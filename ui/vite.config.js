import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'
import { vitePlugin } from 'monaco-editor-nls-adapter';
// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
})
