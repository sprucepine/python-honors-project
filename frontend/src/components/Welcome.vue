<script setup>
</script>

<template>
  <section class="welcome card bg-base-100 shadow-md">
    <h1 class="welcome-title">Welcome to Bubblesheets on the Web (Beta)!</h1>
    <p class="welcome-description">
      Bubblesheets on the web is allows users of the Bubblesheets app to make their bubblesheets on a computer, and then export them to the app for scanning. This web app is currently in early beta.
      </p>  
    <p class="welcome-instructions">
      To get started, simply type something into the input box and click the "Run Python Logic" button. The results will be displayed below the controls.
      Notice: all data is stored locally in your browser and is not shared with anyone. Avoid leaving this site over a long period of time as data may be lost. For the best experience, use a modern browser like Chrome, Firefox, or Edge.
    </p>
  </section>
  </template>
<style scoped>
.welcome {
    padding: 1rem;
    text-align: center;
}
.welcome-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}
.welcome-description {
    font-size: 1rem;
    margin-bottom: 0.75rem;
}
.welcome-instructions {
    font-size: 0.95rem;
    color: color-mix(in oklab, var(--color-base-content) 65%, transparent);
}
</style>