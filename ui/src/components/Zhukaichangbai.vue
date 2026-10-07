<template>
    <div id="zhukaichangbaibox">
        <monaco :options="{
            wordWrap: 'on',
            automaticLayout:true
        }" v-model:value="jsonall.data.data.first_mes" style="border-radius: 8px;overflow: hidden;"
            theme="vs-dark" language="text" />
    </div>
</template>
<script setup name="zhukaichangbai">
import monaco from "monaco-editor-vue3"
import { jsonall } from "../main";
</script>
<style lang="scss" scoped>
#zhukaichangbaibox {
    overflow: hidden;
    width: 100%;
    height: 100%;
}
</style>