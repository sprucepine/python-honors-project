import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import { SaveState, type TaskItem } from '@/types/tasks'

const DEFAULT_TASKS: TaskItem[] = [
  { id: 1, label: 'Review source data' },
  { id: 2, label: 'Clean malformed rows' },
  { id: 3, label: 'Run transformation' },
  { id: 4, label: 'Publish report' },
]

export const useTaskStore = defineStore(
  'tasks',
  () => {
    const tasks = ref<TaskItem[]>([...DEFAULT_TASKS])
    const saveState = ref<SaveState>(SaveState.Idle)

    const saveStatusText = computed(() => {
      if (saveState.value === SaveState.Saving) return 'Saving...'
      if (saveState.value === SaveState.Saved) return 'Saved to browser data'
      if (saveState.value === SaveState.Error) return 'Save failed'
      return ''
    })

    function setTasks(items: TaskItem[]) {
      tasks.value = items
    }

    function setSaveState(state: SaveState) {
      saveState.value = state
    }

    function moveTaskUp(index: number) {
      if (index <= 0) return false

      const current = tasks.value[index]
      const previous = tasks.value[index - 1]
      if (!current || !previous) return false

      tasks.value[index] = previous
      tasks.value[index - 1] = current
      return true
    }

    function moveTaskDown(index: number) {
      if (index >= tasks.value.length - 1) return false

      const current = tasks.value[index]
      const next = tasks.value[index + 1]
      if (!current || !next) return false

      tasks.value[index] = next
      tasks.value[index + 1] = current
      return true
    }

    return {
      tasks,
      saveState,
      saveStatusText,
      setTasks,
      setSaveState,
      moveTaskUp,
      moveTaskDown,
    }
  },
  {
    persist: {
      key: 'honors.tasks',
      storage: localStorage,
      pick: ['tasks'],
    },
  },
)
