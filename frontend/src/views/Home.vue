<template>
  <div class="bg-white">
    <div class="relative isolate px-6 pt-14 lg:px-8">
      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
        <div class="text-center">
          <h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
            Find your dream job with PandaJobs
          </h1>
          <p class="mt-6 text-lg leading-8 text-gray-600">
            Search through thousands of job listings from both local and external sources. 
            Your next career move is just a few clicks away.
          </p>
          <div class="mt-10 flex items-center justify-center gap-x-6">
            <router-link
              to="/jobs"
              class="rounded-md bg-blue-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
            >
              Search Jobs
            </router-link>
            <router-link to="/about" class="text-sm font-semibold leading-6 text-gray-900">
              Learn more <span aria-hidden="true">→</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
