<template>
    <div id="codebox">
        <monaco v-model:value="jsontext" :options="{
            wordWrap: 'on',
            automaticLayout:true
        }" style="border-radius: 8px;overflow: hidden;" theme="vs-dark" language="json" />
    </div>
</template>
<script setup name="code">
import monaco from 'monaco-editor-vue3'
import { jsonall } from '../main';
import { computed } from 'vue';
let jsontext = computed({
    get:()=> JSON.stringify(jsonall.data,null,2),
    set:(x)=> { jsonall.data = JSON.parse(x) }}
)
console.log(JSON.stringify(jsonall.data))
</script>
<style lang="scss">
#codebox {
    width: 100%;
    height: 100%;
}
</style>