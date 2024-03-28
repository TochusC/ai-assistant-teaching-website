<template>
<div id="basic-information">
    <el-divider content-position="left">
        <el-text style="font-size: 22px;">
            基本信息
        </el-text>
    </el-divider>
    <div id="info-container" >
        <div id="left">
            <!-- 显示头像 -->
            <el-avater :size="100" :src="circleUrl"/>
        </div>
        <div id="right">
            <el-text>姓名：11111</el-text>
            <div>
                <span>性别</span>
                <el-radio-group v-model="radio1" >
                    <el-radio value="1" size="small">男</el-radio>
                    <el-radio value="2" size="small">女</el-radio>
                </el-radio-group>
            </div>
            
        </div>
    </div>
</div>

<div id="contact-way">
    <el-divider content-position="left">
        <el-text style="font-size: 22px;">
            联系方式
        </el-text>
    </el-divider>

    <div id="info-container">
        <div>
            <span>Email</span>
            <el-input
            v-model="input1"
            aria-placeholder="您还未绑定邮箱"
            :prefix-icon="Message"
            />
        </div>
        <div>
            <span>手机号</span>
            <el-input
            
            />
        </div>
    </div>
</div>

</template>

<script>
import {reactive,toRefs,ref} from "vue";
import { Message } from "@element-plus/icons-vue/global";
const radio1 = ref('1');
const input1 = ref('');
const state = reactive({
    circleUrl:''
})

const {circleUrl} = toRefs(state)

// const props = defineProps({
//     information:{
//         type:String,
//         required:true
//     }
// })
</script>

<style scoped>
#basic-information{
    width: 100%;
}
#contact-way{
    width: 100%;
}
.left{
    flex: 1;
}
.right {
  flex: 1; /* 设置左右两个部分平均占据容器的宽度 */
}
</style>