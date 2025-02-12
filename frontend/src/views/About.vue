<template>
  <div class="bg-white py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:text-center">
        <h2 class="text-base font-semibold leading-7 text-blue-600">About PandaJobs</h2>
        <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
          Everything you need to find your next job
        </p>
        <p class="mt-6 text-lg leading-8 text-gray-600">
          PandaJobs is your one-stop platform for job searching, combining both local and external job listings 
          to provide you with the most comprehensive job search experience.
        </p>
      </div>
      <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
        <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16">
          <div class="relative pl-16">
            <dt class="text-base font-semibold leading-7 text-gray-900">
              <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-blue-600">
                <MagnifyingGlassIcon class="h-6 w-6 text-white" aria-hidden="true" />
              </div>
              Comprehensive Search
            </dt>
            <dd class="mt-2 text-base leading-7 text-gray-600">
              Search through thousands of job listings from both our local database and external job boards.
            </dd>
          </div>
          <div class="relative pl-16">
            <dt class="text-base font-semibold leading-7 text-gray-900">
              <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-blue-600">
                <BoltIcon class="h-6 w-6 text-white" aria-hidden="true" />
              </div>
              Real-time Updates
            </dt>
            <dd class="mt-2 text-base leading-7 text-gray-600">
              Get instant access to new job postings as they become available.
            </dd>
          </div>
          <div class="relative pl-16">
            <dt class="text-base font-semibold leading-7 text-gray-900">
              <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-blue-600">
                <UserGroupIcon class="h-6 w-6 text-white" aria-hidden="true" />
              </div>
              Direct Applications
            </dt>
            <dd class="mt-2 text-base leading-7 text-gray-600">
              Apply directly to jobs through our platform, making the application process seamless.
            </dd>
          </div>
          <div class="relative pl-16">
            <dt class="text-base font-semibold leading-7 text-gray-900">
              <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-blue-600">
                <BellAlertIcon class="h-6 w-6 text-white" aria-hidden="true" />
              </div>
              Job Alerts
            </dt>
            <dd class="mt-2 text-base leading-7 text-gray-600">
              Set up custom job alerts to get notified when new positions matching your criteria are posted.
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </div>
</template>

<script setup>
import { MagnifyingGlassIcon, BoltIcon, UserGroupIcon, BellAlertIcon } from '@heroicons/vue/24/outline'
</script>
