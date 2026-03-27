<script setup>
import { ref } from 'vue'

const input = ref('')
const result = ref(null)

async function runLogic() {
  // No complex URLs needed because of the Proxy!
  const response = await fetch(`/api/process?text=${input.value}`)
  result.value = await response.json()
}
</script>

<template>
  <div style="padding: 20px;">
    <input class="input input-bordered" v-model="input" placeholder="Type something..." />
    <button class="btn btn-primary" @click="runLogic">Run Python Logic</button>

    <div class="card" v-if="result" style="margin-top: 20px;">
      <p>Result: {{ result.processed_text }}</p>
      <p>Chars: {{ result.length }}</p>
    </div>
  </div>
</template>