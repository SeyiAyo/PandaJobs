<template>
  <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
    <!-- Search Form -->
    <div class="bg-white rounded-lg shadow-sm p-6 mb-8">
      <h2 class="text-2xl font-bold text-gray-900 mb-6">Search Jobs</h2>
      <form @submit.prevent="performSearch" class="space-y-4">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label for="query" class="block text-sm font-medium text-gray-700">Keywords</label>
            <input
              type="text"
              v-model="searchParams.query"
              name="query"
              id="query"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
          </div>
          <div>
            <label for="location" class="block text-sm font-medium text-gray-700">Location</label>
            <input
              type="text"
              v-model="searchParams.location"
              name="location"
              id="location"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
          </div>
          <div>
            <label for="source" class="block text-sm font-medium text-gray-700">Search Source</label>
            <select
              v-model="searchParams.source"
              name="source"
              id="source"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            >
              <option value="local">Local Jobs</option>
              <option value="external">External Jobs</option>
            </select>
          </div>
        </div>
        <div class="flex justify-end">
          <button
            type="submit"
            :disabled="isLoading"
            class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50"
          >
            <span v-if="isLoading">Searching...</span>
            <span v-else>Search Jobs</span>
          </button>
        </div>
      </form>
    </div>

    <!-- Loading State -->
    <div v-if="isLoading" class="flex justify-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-red-50 border-l-4 border-red-400 p-4 mb-4">
      <div class="flex">
        <div class="flex-shrink-0">
          <ExclamationCircleIcon class="h-5 w-5 text-red-400" aria-hidden="true" />
        </div>
        <div class="ml-3">
          <p class="text-sm text-red-700">{{ error }}</p>
        </div>
      </div>
    </div>

    <!-- Results -->
    <div v-else-if="jobs.length > 0" class="space-y-4">
      <div v-for="job in jobs" :key="job.id" class="bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200">
        <a :href="job.url" class="block p-6" :target="job.source === 'external' ? '_blank' : '_self'">
          <div class="flex justify-between items-start">
            <div class="flex-1">
              <div class="flex items-center">
                <h3 class="text-xl font-semibold text-gray-900">{{ job.title }}</h3>
                <span
                  :class="[
                    'ml-2 px-2 py-1 text-xs font-medium rounded-full',
                    job.source === 'external' ? 'bg-purple-100 text-purple-800' : 'bg-green-100 text-green-800',
                  ]"
                >
                  {{ job.source === 'external' ? 'External' : 'Local' }}
                </span>
              </div>
              <div class="mt-2 flex items-center text-gray-600 text-sm">
                <span class="mr-4">
                  <BuildingOfficeIcon class="inline-block h-4 w-4 mr-1" />
                  {{ job.company_name }}
                </span>
                <span v-if="job.company_location">
                  <MapPinIcon class="inline-block h-4 w-4 mr-1" />
                  {{ job.company_location }}
                </span>
              </div>
              <div v-if="job.job_type" class="mt-2 text-sm text-gray-600">
                <BriefcaseIcon class="inline-block h-4 w-4 mr-1" />
                {{ job.job_type }}
              </div>
              <div v-if="job.salary" class="mt-2 text-sm text-gray-600">
                <CurrencyDollarIcon class="inline-block h-4 w-4 mr-1" />
                {{ job.salary }}
              </div>
            </div>
          </div>
        </a>
      </div>

      <!-- Load More Button -->
      <div v-if="hasNextPage" class="text-center mt-8">
        <button
          @click="loadMore"
          :disabled="isLoading"
          class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50"
        >
          <span v-if="isLoading">Loading...</span>
          <span v-else>Load More</span>
        </button>
      </div>
    </div>

    <!-- No Results -->
    <div v-else-if="!isLoading" class="text-center py-12">
      <div class="text-gray-400 mb-4">
        <MagnifyingGlassIcon class="mx-auto h-12 w-12" />
      </div>
      <h3 class="text-xl font-semibold text-gray-900 mb-2">No jobs found</h3>
      <p class="text-gray-600">Try adjusting your search criteria</p>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import axios from 'axios'
import {
  BuildingOfficeIcon,
  MapPinIcon,
  BriefcaseIcon,
  CurrencyDollarIcon,
  ExclamationCircleIcon,
  MagnifyingGlassIcon,
} from '@heroicons/vue/24/outline'

const jobs = ref([])
const isLoading = ref(false)
const error = ref(null)
const currentPage = ref(1)
const hasNextPage = ref(false)

const searchParams = reactive({
  query: '',
  location: '',
  source: 'local',
})

async function performSearch(append = false) {
  if (!append) {
    currentPage.value = 1
    jobs.value = []
  }
  
  isLoading.value = true
  error.value = null

  try {
    const params = new URLSearchParams({
      query: searchParams.query,
      location: searchParams.location,
      source: searchParams.source,
      page: currentPage.value,
    })

    const response = await axios.get(`/jobs/api/search/?${params}`)
    
    if (append) {
      jobs.value.push(...response.data.jobs)
    } else {
      jobs.value = response.data.jobs
    }
    
    hasNextPage.value = response.data.has_next
  } catch (e) {
    error.value = 'An error occurred while searching for jobs'
    console.error('Search error:', e)
  } finally {
    isLoading.value = false
  }
}

async function loadMore() {
  currentPage.value++
  await performSearch(true)
}
</script>
