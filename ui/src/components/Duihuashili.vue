<template>
    <div id="duihuashili">
        <monaco :options="{
            wordWrap: 'on',
            automaticLayout:true
        }" v-model:value="jsonall.data.data.mes_example" style="border-radius: 8px;overflow: hidden;"
            theme="vs-dark" language="text" />
    </div>
</template>
<script setup name="duihuashili">
import monaco from "monaco-editor-vue3"
import { jsonall } from "../main";
</script>
<style lang="scss" scoped>
#duihuashili {
    overflow: hidden;
    width: 100%;
    height: 100%;
}
</style>