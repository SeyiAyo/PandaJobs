<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <h1 class="text-3xl font-bold mb-6">Add Job</h1>

    <!-- Error Messages -->
    <div
      v-if="errors.length > 0"
      class="bg-red-50 border-l-4 border-red-400 p-4 mb-6"
    >
      <div class="flex">
        <ExclamationCircleIcon class="h-5 w-5 text-red-400" />
        <div class="ml-3">
          <p
            v-for="error in errors"
            :key="error"
            class="text-sm text-red-700"
          >
            {{ error }}
          </p>
        </div>
      </div>
    </div>

    <!-- Job Form -->
    <form @submit.prevent="submitForm" class="bg-white shadow-md rounded-lg px-8 pt-6 pb-8 mb-4">
      <div class="space-y-6">
        <!-- Title -->
        <div>
          <label
            for="title"
            class="block text-sm font-medium leading-6 text-gray-900"
          >
            Title
          </label>
          <div class="mt-2">
            <input
              v-model="formData.title"
              type="text"
              name="title"
              id="title"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6"
              :class="{ 'ring-red-300': v$.title.$error }"
            />
            <p
              v-if="v$.title.$error"
              class="mt-2 text-sm text-red-600"
            >
              {{ v$.title.$errors[0].$message }}
            </p>
          </div>
        </div>

        <!-- Summary -->
        <div>
          <label
            for="summary"
            class="block text-sm font-medium leading-6 text-gray-900"
          >
            Summary
          </label>
          <div class="mt-2">
            <textarea
              v-model="formData.summary"
              name="summary"
              id="summary"
              rows="3"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6"
              :class="{ 'ring-red-300': v$.summary.$error }"
            />
            <p
              v-if="v$.summary.$error"
              class="mt-2 text-sm text-red-600"
            >
              {{ v$.summary.$errors[0].$message }}
            </p>
          </div>
        </div>

        <!-- Full Description -->
        <div>
          <label
            for="full_description"
            class="block text-sm font-medium leading-6 text-gray-900"
          >
            Full Description
          </label>
          <div class="mt-2">
            <textarea
              v-model="formData.full_description"
              name="full_description"
              id="full_description"
              rows="6"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6"
              :class="{ 'ring-red-300': v$.full_description.$error }"
            />
            <p
              v-if="v$.full_description.$error"
              class="mt-2 text-sm text-red-600"
            >
              {{ v$.full_description.$errors[0].$message }}
            </p>
          </div>
        </div>

        <!-- Company Details -->
        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
          <!-- Company Name -->
          <div>
            <label
              for="company_name"
              class="block text-sm font-medium leading-6 text-gray-900"
            >
              Company Name
            </label>
            <div class="mt-2">
              <input
                v-model="formData.company_name"
                type="text"
                name="company_name"
                id="company_name"
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6"
                :class="{ 'ring-red-300': v$.company_name.$error }"
              />
              <p
                v-if="v$.company_name.$error"
                class="mt-2 text-sm text-red-600"
              >
                {{ v$.company_name.$errors[0].$message }}
              </p>
            </div>
          </div>

          <!-- Company Location -->
          <div>
            <label
              for="company_location"
              class="block text-sm font-medium leading-6 text-gray-900"
            >
              Company Location
            </label>
            <div class="mt-2">
              <input
                v-model="formData.company_location"
                type="text"
                name="company_location"
                id="company_location"
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          <!-- Company Country -->
          <div>
            <label
              for="company_country"
              class="block text-sm font-medium leading-6 text-gray-900"
            >
              Country
            </label>
            <div class="mt-2">
              <select
                v-model="formData.company_country"
                name="company_country"
                id="company_country"
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6"
              >
                <option
                  v-for="[code, name] in Object.entries(countries)"
                  :key="code"
                  :value="code"
                >
                  {{ name }}
                </option>
              </select>
            </div>
          </div>

          <!-- Company Size -->
          <div>
            <label
              for="company_size"
              class="block text-sm font-medium leading-6 text-gray-900"
            >
              Company Size
            </label>
            <div class="mt-2">
              <select
                v-model="formData.company_size"
                name="company_size"
                id="company_size"
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6"
                :class="{ 'ring-red-300': v$.company_size.$error }"
              >
                <option value="size_1_9">1-9 employees</option>
                <option value="size_10_49">10-49 employees</option>
                <option value="size_50_99">50-99 employees</option>
                <option value="size_100">100+ employees</option>
              </select>
              <p
                v-if="v$.company_size.$error"
                class="mt-2 text-sm text-red-600"
              >
                {{ v$.company_size.$errors[0].$message }}
              </p>
            </div>
          </div>
        </div>

        <!-- Submit Button -->
        <div class="flex justify-end">
          <button
            type="submit"
            :disabled="isSubmitting"
            class="rounded-md bg-blue-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 disabled:opacity-50"
          >
            <span v-if="isSubmitting">Submitting...</span>
            <span v-else>Submit Job</span>
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useVuelidate } from '@vuelidate/core'
import { required, minLength } from '@vuelidate/validators'
import axios from 'axios'
import { ExclamationCircleIcon } from '@heroicons/vue/24/outline'

const router = useRouter()
const isSubmitting = ref(false)
const errors = ref([])

const formData = reactive({
  title: '',
  summary: '',
  full_description: '',
  company_name: '',
  company_location: '',
  company_country: 'GB',  // Default to UK
  company_size: '',
})

const rules = {
  title: { required, minLength: minLength(5) },
  summary: { required, minLength: minLength(20) },
  full_description: { required, minLength: minLength(50) },
  company_name: { required },
  company_size: { required },
}

const v$ = useVuelidate(rules, formData)

// List of countries (you can fetch this from an API or import from a file)
const countries = {
  GB: 'United Kingdom',
  US: 'United States',
  // Add more countries as needed
}

async function submitForm() {
  errors.value = []
  isSubmitting.value = true

  try {
    const result = await v$.value.$validate()
    if (!result) {
      return
    }

    const response = await axios.post('/jobs/api/jobs/', formData)
    router.push({
      name: 'job-detail',
      params: { id: response.data.id },
    })
  } catch (error) {
    if (error.response?.data) {
      // Handle validation errors from the server
      Object.entries(error.response.data).forEach(([field, messages]) => {
        errors.value.push(`${field}: ${messages.join(', ')}`)
      })
    } else {
      errors.value.push('An error occurred while submitting the job. Please try again.')
    }
  } finally {
    isSubmitting.value = false
  }
}
</script>
