
import { createApp } from 'vue'
import "/all.scss"
import { reactive, ref } from 'vue'
import App from './App.vue'
export const 保存状态= ref(-1)
export const jsonall = reactive({
    data: JSON.parse('{"data":{"alternate_greetings":[],"character_book":{"description":"","enabled":false,"entries":[],"global_constant":true,"name":"","scan_depth":101,"token_budget":1536,"token_budget_enabled":false},"creator_notes":"","description":"","extensions":{"piupiu_regex":{"enabled":true,"ignoreEmptyReplace":false,"scripts":[]},"regex_scripts":[]},"first_mes":"","mes_example":"","message_style_tags":[],"name":"","post_history_instructions":"","system_prompt":"","tags":[]},"spec":"chara_card_v2","spec_version":"2.0"}')
})
createApp(App).mount('#app')
