<script setup>
const logo = '/logo.svg';
</script>
<template>
  <div class="navbar bg-base-100 nav-wrap">
    <div class="navbar-start">
    <a class="btn btn-ghost normal-case nav-brand gap-2" href="#" aria-label="Bubblesheets on the Web home">
      <img :src="logo" aria-hidden="true" class="logo" />
      <span>Bubblesheets on the Web</span>
    </a>
  </div>
    <div class="navbar-end">
      
      <ul class="menu menu-horizontal px-1">
        <li>
          <details>
            <summary>
              <iconify-icon icon="lucide:github" width="18" height="18"></iconify-icon>
            </summary>
            <ul class="bg-base-100 rounded-box right-0 w-56 p-2 shadow">
              <li>
                <a href="https://github.com/sprucepine/bubblesheets" target="_blank" rel="noopener noreferrer" class="flex items-center justify-between gap-2" aria-label="Swift app repository (opens in new tab)" >
                  <span>Swift App Repository</span>
                  <iconify-icon icon="lucide:external-link" width="14" height="14" aria-hidden="true" title="Opens in a new tab"></iconify-icon>
                </a>
              </li>
              <li>
                <a href="https://github.com" target="_blank" rel="noopener noreferrer" class="flex items-center justify-between gap-2" aria-label="Web app repository (opens in new tab)">
                  <span>Web App Repository</span>
                  <iconify-icon icon="lucide:external-link" width="14" height="14" aria-label="Opens in new tab" title="Opens in a new tab"></iconify-icon>
                </a>
              </li>
            </ul>
          </details>
        </li>
      </ul>
 
  </div>
  </div>

</template>

<style scoped>
.nav-wrap {
  display: flex;
  align-items: center;
  padding: 0.55rem 1rem;
  border-bottom: 1px solid color-mix(in oklab, var(--color-base-content) 10%, transparent);
}

.logo {
  width: 1.4rem;
  height: 1.4rem;
}

.nav-brand {
  padding-inline: 0.6rem;
  font-size: 1.16rem;
  font-weight: 600;
  transition: background-color 150ms ease, transform 150ms ease;
}

.nav-brand:hover,
.nav-brand:focus-visible {
  transform: translateY(-1px);
}

@media (max-width: 640px) {
  .nav-wrap {
    padding: 0.5rem 0.7rem;
  }

  .nav-brand {
    padding-inline: 0.35rem;
    font-size: 1.04rem;
  }
}
</style>    