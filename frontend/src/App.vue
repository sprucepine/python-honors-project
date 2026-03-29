<script setup lang="ts">
import { onMounted, ref } from 'vue'
import draggable from 'vuedraggable'
import Header from '@/components/Header.vue'

type TaskItem = {
  id: number
  label: string
}

type ProcessResult = {
  processed_text: string
  length: number
}

const input = ref('')
const result = ref<ProcessResult | null>(null)
const tasks = ref<TaskItem[]>([])
const tasksError = ref('')
const saveStatus = ref('')
const ariaLiveRegionId = 'task-status-region'

async function runLogic() {
  const response = await fetch(`/api/process?text=${encodeURIComponent(input.value)}`)
  result.value = await response.json()
}

async function loadTasks() {
  tasksError.value = ''

  try {
    const response = await fetch('/api/tasks')
    if (!response.ok) {
      throw new Error('Failed to load tasks')
    }

    const data = await response.json()
    tasks.value = data.items
  } catch {
    tasksError.value = 'Could not load tasks from Python backend.'
  }
}

async function persistOrder() {
  saveStatus.value = 'Saving order...'

  try {
    const response = await fetch('/api/tasks/reorder', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ items: tasks.value }),
    })

    if (!response.ok) {
      throw new Error('Failed to save task order')
    }

    const data = await response.json()
    tasks.value = data.items
    saveStatus.value = 'Order saved'
  } catch {
    saveStatus.value = 'Save failed'
  }
}

function moveTaskUp(index: number) {
  if (index > 0) {
    const temp = tasks.value[index]
    tasks.value[index] = tasks.value[index - 1]
    tasks.value[index - 1] = temp
    persistOrder()
  }
}

function moveTaskDown(index: number) {
  if (index < tasks.value.length - 1) {
    const temp = tasks.value[index]
    tasks.value[index] = tasks.value[index + 1]
    tasks.value[index + 1] = temp
    persistOrder()
  }
}

onMounted(loadTasks)
</script>

<template>
  <Header />

  <main class="page">
    <section class="panel card bg-base-100 shadow-md">
      <h2 class="panel-title">Python Logic Demo</h2>
      <div class="logic-controls">
        <label for="logic-input" class="sr-only">Text input for Python logic</label>
        <input
          id="logic-input"
          class="input input-bordered"
          v-model="input"
          placeholder="Type something..."
          aria-describedby="logic-desc"
        />
        <p id="logic-desc" class="sr-only">Enter text to be processed by the Python logic engine.</p>
        <button class="btn btn-primary" @click="runLogic" aria-label="Run Python logic to process text">
          <iconify-icon icon="lucide:sparkles" width="18" height="18" aria-hidden="true"></iconify-icon>
          Run Python Logic
        </button>
      </div>

      <div class="result" v-if="result" role="region" aria-live="polite" aria-label="Logic result">
        <p><strong>Result:</strong> {{ result.processed_text }}</p>
        <p><strong>Character count:</strong> {{ result.length }}</p>
      </div>
    </section>

    <section class="panel card bg-base-100 shadow-md">
      <div class="tasks-heading">
        <h2 class="panel-title">Drag and Drop Tasks</h2>
        <span class="status" v-if="saveStatus">{{ saveStatus }}</span>
      </div>

      <div
        v-if="tasksError"
        class="error"
        role="alert"
        aria-live="assertive"
      >
        {{ tasksError }}
      </div>

      <div class="sr-only" id="task-status-region" role="status" aria-live="polite" aria-atomic="true">
        {{ saveStatus }}
      </div>

      <p class="keyboard-hint">Tip: Use arrow keys to move tasks, or drag with your mouse.</p>

      <draggable
        v-model="tasks"
        item-key="id"
        handle=".drag-handle"
        ghost-class="ghost"
        :animation="180"
        @end="persistOrder"
        role="list"
        :aria-label="`${tasks.length} tasks to organize`"
        tabindex="0"
      >
        <template #item="{ element, index }">
          <article class="task-row" role="listitem">
            <button
              class="drag-handle btn btn-ghost btn-sm"
              type="button"
              style="cursor: grab"
              :aria-label="`Drag ${element.label} to reorder`"
              :aria-describedby="`task-${element.id}-actions`"
              tabindex="0"
              @keydown.down="moveTaskDown(index)"
              @keydown.up="moveTaskUp(index)"
            >
              <iconify-icon icon="lucide:grip-vertical" width="16" height="16" aria-hidden="true"></iconify-icon>
            </button>
            <span class="task-label">{{ element.label }}</span>
            <div :id="`task-${element.id}-actions`" class="task-actions">
              <button
                class="btn btn-ghost btn-xs"
                type="button"
                @click="moveTaskUp(index)"
                :disabled="index === 0"
                :aria-label="`Move ${element.label} up`"
                title="Move up (disabled if already first)"
              >
                <iconify-icon icon="lucide:arrow-up" width="14" height="14" aria-hidden="true"></iconify-icon>
              </button>
              <button
                class="btn btn-ghost btn-xs"
                type="button"
                @click="moveTaskDown(index)"
                :disabled="index === tasks.length - 1"
                :aria-label="`Move ${element.label} down`"
                title="Move down (disabled if already last)"
              >
                <iconify-icon icon="lucide:arrow-down" width="14" height="14" aria-hidden="true"></iconify-icon>
              </button>
            </div>
          </article>
        </template>
      </draggable>
    </section>
  </main>
</template>

<style scoped>
.page {
  padding: 1rem;
  display: grid;
  gap: 1rem;
  max-width: 760px;
  margin: 0 auto;
}

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

.tasks-heading {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.status {
  font-size: 0.85rem;
  color: color-mix(in oklab, var(--color-base-content) 65%, transparent);
}

.error {
  color: #b42318;
  margin-bottom: 0.5rem;
}

.task-row {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  border: 1px solid color-mix(in oklab, var(--color-base-content) 16%, transparent);
  border-radius: 0.55rem;
  padding: 0.45rem 0.6rem;
  margin-bottom: 0.55rem;
  background: var(--color-base-100);
}

.ghost {
  opacity: 0.5;
  background-color: color-mix(in oklab, var(--color-base-content) 5%, transparent);
}

.task-label {
  flex: 1;
  word-break: break-word;
}

.task-actions {
  display: flex;
  gap: 0.3rem;
  margin-left: auto;
}

.keyboard-hint {
  font-size: 0.875rem;
  color: color-mix(in oklab, var(--color-base-content) 60%, transparent);
  margin-bottom: 0.75rem;
  padding: 0.5rem;
  background-color: color-mix(in oklab, var(--color-primary) 10%, transparent);
  border-radius: 0.375rem;
}

/* Screen reader only content */
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

/* Enhanced focus indicators for keyboard navigation */
button:focus-visible,
input:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* High contrast for disabled buttons */
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Ensure text has sufficient contrast */
.error {
  background-color: color-mix(in oklab, #b42318 15%, transparent);
  padding: 0.75rem;
  border-radius: 0.375rem;
  border-left: 4px solid #b42318;
}

@media (max-width: 640px) {
  .page {
    padding: 0.75rem;
  }

  .task-actions {
    gap: 0.2rem;
  }

  .task-row {
    flex-wrap: wrap;
  }
}
</style>