<template>
<label>
    <input type="checkbox" class="input" :checked="props.v==true?jsonall.data.data.character_book.enabled:jsonall.data.data.character_book.global_constant" @change="handleChange">
    <span class="custom-checkbox"></span>
  </label>
</template>
<script setup name="Fuxuankuang_shijieshu">
import { jsonall } from '../main';

const props = defineProps(["v"]);

// 3. 处理变化，通知父组件更新
const handleChange = (event) => {
  if(props.v==true){
    jsonall.data.data.character_book.enabled=!jsonall.data.data.character_book.enabled;
  }else{
    jsonall.data.data.character_book.global_constant=!jsonall.data.data.character_book.global_constant;
  }
  console.log(jsonall.data.data.character_book.enabled,jsonall.data.data.character_book.global_constant);
};

</script>
<style lang="scss" scoped>
/* From Uiverse.io by PriyanshuGupta28 */ 
.input[type="checkbox"] {
  display: none;
}


  /* Style for the custom checkbox */
.custom-checkbox {
  display: inline-block;
  width: 15px;
  height: 15px;
  border: 2px solid #FFFFFF;
  border-radius: 4px;
  position: relative;
  cursor: pointer;
}

  /* Style for the custom checkmark */
.custom-checkbox::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 10px;
  height: 10px;
  background-color: #FFFFFF;
  border-radius: 2px;
  opacity: 0;
}

  /* Show the checkmark when checkbox is checked */
.input[type="checkbox"]:checked + .custom-checkbox::after {
  opacity: 1;
}
</style>