<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div v-if="isLoading" class="flex justify-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
    </div>

    <div v-else-if="error" class="bg-red-50 border-l-4 border-red-400 p-4">
      <div class="flex">
        <ExclamationCircleIcon class="h-5 w-5 text-red-400" />
        <div class="ml-3">
          <p class="text-sm text-red-700">{{ error }}</p>
        </div>
      </div>
    </div>

    <div v-else-if="job" class="bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Header Section -->
      <div class="bg-blue-600 text-white p-6">
        <div class="flex justify-between items-start">
          <div>
            <h1 class="text-3xl font-bold mb-2">{{ job.title }}</h1>
            <div class="flex items-center space-x-4 text-blue-100">
              <span class="flex items-center">
                <BuildingOfficeIcon class="h-5 w-5 mr-2" />
                {{ job.company_name }}
              </span>
              <span v-if="job.company_location" class="flex items-center">
                <MapPinIcon class="h-5 w-5 mr-2" />
                {{ job.company_location }}
              </span>
              <span v-if="job.company_size" class="flex items-center">
                <UsersIcon class="h-5 w-5 mr-2" />
                {{ job.company_size }}
              </span>
            </div>
          </div>
          <div class="flex items-center space-x-2">
            <span class="px-3 py-1 bg-blue-500 rounded-full text-sm font-semibold">
              {{ job.status }}
            </span>
          </div>
        </div>
      </div>

      <!-- Job Details -->
      <div class="p-6">
        <!-- Quick Info -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
          <div class="bg-gray-50 p-4 rounded-lg">
            <div class="text-gray-600 text-sm">Salary Range</div>
            <div class="font-semibold">
              {{ job.salary || 'Not specified' }}
            </div>
          </div>
          <div class="bg-gray-50 p-4 rounded-lg">
            <div class="text-gray-600 text-sm">Work Type</div>
            <div class="font-semibold flex items-center">
              <component
                :is="workTypeIcon"
                v-if="workTypeIcon"
                class="h-5 w-5 mr-2"
              />
              {{ job.work_type || 'Not specified' }}
            </div>
          </div>
          <div class="bg-gray-50 p-4 rounded-lg">
            <div class="text-gray-600 text-sm">Posted</div>
            <div class="font-semibold">{{ formattedDate }}</div>
          </div>
        </div>

        <!-- Description -->
        <div class="mb-8">
          <h2 class="text-xl font-semibold mb-4">Description</h2>
          <div class="prose max-w-none" v-html="formattedDescription"></div>
        </div>

        <!-- Apply Button -->
        <div class="flex justify-center">
          <button
            v-if="job.status === 'open'"
            @click="applyForJob"
            class="inline-flex items-center px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-300"
          >
            <PaperAirplaneIcon class="h-5 w-5 mr-2" />
            Apply for this Position
          </button>
          <div v-else class="text-center p-4 bg-gray-100 rounded-lg">
            <LockClosedIcon class="h-8 w-8 mx-auto text-gray-500 mb-2" />
            <p class="text-gray-600">This position is no longer accepting applications</p>
          </div>
        </div>
      </div>

      <!-- Share and Save -->
      <div class="border-t border-gray-200 p-6 bg-gray-50">
        <div class="flex justify-between items-center">
          <div class="flex space-x-4">
            <button
              @click="saveJob"
              class="text-gray-600 hover:text-blue-600 transition flex items-center"
            >
              <BookmarkIcon class="h-5 w-5 mr-2" />
              Save Job
            </button>
            <button
              @click="shareJob"
              class="text-gray-600 hover:text-blue-600 transition flex items-center"
            >
              <ShareIcon class="h-5 w-5 mr-2" />
              Share
            </button>
          </div>
          <div class="text-gray-500 text-sm">
            Job ID: {{ job.id }}
          </div>
        </div>
      </div>
    </div>

    <!-- Similar Jobs -->
    <div v-if="similarJobs.length > 0" class="mt-8">
      <h2 class="text-2xl font-semibold mb-4">Similar Jobs</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <router-link
          v-for="job in similarJobs"
          :key="job.id"
          :to="{ name: 'job-detail', params: { id: job.id }}"
          class="block bg-white rounded-lg shadow-sm hover:shadow-md transition p-4"
        >
          <h3 class="font-semibold text-lg mb-2">{{ job.title }}</h3>
          <div class="text-gray-600 text-sm flex items-center space-x-4">
            <span class="flex items-center">
              <BuildingOfficeIcon class="h-4 w-4 mr-1" />
              {{ job.company_name }}
            </span>
            <span v-if="job.company_location" class="flex items-center">
              <MapPinIcon class="h-4 w-4 mr-1" />
              {{ job.company_location }}
            </span>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import {
  BuildingOfficeIcon,
  MapPinIcon,
  UsersIcon,
  PaperAirplaneIcon,
  LockClosedIcon,
  BookmarkIcon,
  ShareIcon,
  ExclamationCircleIcon,
  ComputerDesktopIcon,
  BuildingOffice2Icon,
  ArrowPathRoundedSquareIcon,
} from '@heroicons/vue/24/outline'
import { format } from 'date-fns'

const route = useRoute()
const router = useRouter()
const job = ref(null)
const similarJobs = ref([])
const isLoading = ref(true)
const error = ref(null)

const workTypeIcon = computed(() => {
  if (!job.value?.work_type) return null
  const icons = {
    remote: ComputerDesktopIcon,
    onsite: BuildingOffice2Icon,
    hybrid: ArrowPathRoundedSquareIcon,
  }
  return icons[job.value.work_type]
})

const formattedDate = computed(() => {
  if (!job.value?.created_at) return ''
  return format(new Date(job.value.created_at), 'PPP')
})

const formattedDescription = computed(() => {
  if (!job.value?.description) return ''
  return job.value.description.replace(/\n/g, '<br>')
})

async function fetchJobDetails() {
  isLoading.value = true
  error.value = null
  
  try {
    const response = await axios.get(`/jobs/api/jobs/${route.params.id}/`)
    job.value = response.data
    
    // Fetch similar jobs
    const similarResponse = await axios.get(`/jobs/api/jobs/${route.params.id}/similar/`)
    similarJobs.value = similarResponse.data
  } catch (e) {
    error.value = 'Failed to load job details'
    console.error('Error fetching job details:', e)
  } finally {
    isLoading.value = false
  }
}

async function applyForJob() {
  try {
    const response = await axios.post(`/jobs/api/jobs/${route.params.id}/apply/`)
    if (response.data.redirect) {
      window.location.href = response.data.redirect
    }
  } catch (e) {
    console.error('Error applying for job:', e)
  }
}

function saveJob() {
  // TODO: Implement job saving functionality
  console.log('Save job clicked')
}

function shareJob() {
  if (navigator.share) {
    navigator.share({
      title: job.value.title,
      text: `Check out this job: ${job.value.title} at ${job.value.company_name}`,
      url: window.location.href,
    })
  }
}

onMounted(() => {
  fetchJobDetails()
})
</script>
