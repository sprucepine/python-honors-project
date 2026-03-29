export type TaskItem = {
  id: number
  label: string
}

// String enums are easy to persist and debug in localStorage.
export enum SaveState {
  Idle = 'idle',
  Saving = 'saving',
  Saved = 'saved',
  Error = 'error',
}
