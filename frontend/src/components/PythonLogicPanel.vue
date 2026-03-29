<script setup lang="ts">
import { ref } from 'vue'

type ProcessResult = {
  processed_text: string
  length: number
}

const input = ref('')
const result = ref<ProcessResult | null>(null)

async function runLogic() {
  // Mirror backend demo behavior directly in TS for static hosting.
  const processed_text = input.value.split('').reverse().join('').toUpperCase()
  result.value = {
    processed_text,
    length: input.value.length,
  }
}
</script>

<template>
  <section class="panel card bg-base-100 shadow-md">
    <h2 class="panel-title">Logic Demo (TypeScript)</h2>
    <div class="logic-controls">
      <label for="logic-input" class="sr-only">Text input for TypeScript logic</label>
      <input
        id="logic-input"
        class="input input-bordered"
        v-model="input"
        placeholder="Type something..."
        aria-describedby="logic-desc"
      />
      <p id="logic-desc" class="sr-only">Enter text to be processed by the TypeScript logic engine.</p>
      <button class="btn btn-primary" @click="runLogic" aria-label="Run TypeScript logic to process text">
        <iconify-icon icon="lucide:sparkles" width="18" height="18" aria-hidden="true"></iconify-icon>
        Run Logic
      </button>
    </div>

    <div class="result" v-if="result" role="region" aria-live="polite" aria-label="Logic result">
      <p><strong>Result:</strong> {{ result.processed_text }}</p>
      <p><strong>Character count:</strong> {{ result.length }}</p>
    </div>
  </section>
</template>

<style scoped>
.panel {
  padding: 1rem;
}

.panel-title {
  font-size: 1.05rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
}

.logic-controls {
  display: grid;
  gap: 0.6rem;
}

.result {
  margin-top: 0.8rem;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

button:focus-visible,
input:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
</style>
