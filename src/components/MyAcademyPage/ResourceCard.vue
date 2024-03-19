<script setup lang="ts">
import {DataAnalysis, Document, VideoPlay} from "@element-plus/icons-vue";
import {inject, onMounted, ref} from "vue";

const props = defineProps({
  resource_type: {
    type: String,
    required: true
  },
  resource: {
    type: Object,
    required: true
  },
  resource_root: {
    type: String,
    required: true
  }
})

const cdnServerUrl = inject('cdnServerUrl')

const showPreview = ref(false)
const handleDownload = () => {
  window.open(props.resource_root + props.resource.url)
}

let previewUrl = ''
onMounted(()=>{
  if(props.resource?.hasOwnProperty('preview')){
    previewUrl = props.resource_root + props.resource.preview;
  }
  else {
    previewUrl = props.resource_root + props.resource.url;
  }
  console.log(previewUrl)
})

</script>
<template>
  <el-card id="course-card" style="margin-bottom: 24px">
    <div class="Space-Between-Flex">
      <div id="resource-logo" class="Center-Flex">
       <el-icon  size="36" color="#f2f2f2">
         <VideoPlay v-if="props.resource_type === 'video'" />
         <DataAnalysis v-else-if="props.resource_type === 'ppt'" />
         <Document v-else/>
       </el-icon>
      </div>
      <div id="info-container">
        <div class="Space-Between-Flex">
          <h3>{{ props.resource.name }}</h3>
          <div class="Center-Flex" style="flex-direction: column">

            <div class="Space-Between-Flex" style="margin-bottom: 12px;">
              <el-tag type="info" effect="plain" style="margin-right: 8px">
                {{ props.resource.size }}
              </el-tag>
              <el-tag type="info" effect="plain">
                {{ props.resource.update_date }}
              </el-tag>
            </div>

            <div style="display: flex;width: 100%;align-items: flex-start">
              <el-button type="primary" @click="showPreview=true">
                预览
              </el-button>
              <el-button type="success" @click="handleDownload">
                下载
              </el-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </el-card>
  <el-dialog :draggable="true" v-model="showPreview" >
    <iframe  v-if="props.resource_type !== 'video'" allowfullscreen :src="previewUrl" style="width: 100%; height: 720px;"/>
    <video autoplay controls preload="auto"  v-if="props.resource_type === 'video'">
      <source :src="previewUrl" type="video/mp4">
    </video>

  </el-dialog>
</template>

<style scoped>

#info-container{
  width: 100%;
  height: 100%;
}

#resource-logo{
  width: 96px;
  height: 64px;
  background: #8080FF;
  border: 1px solid #efefef;
  border-radius: 8px;
  margin-right: 8px;
}

#course-card{
  padding: 0;
  margin: 12px;
  transition: 0.2s;
  box-shadow: 0 0 1px #1a1a1a;
}

#course-card:hover{
  transition: 0.2s;
  box-shadow: 0 0 4px #1a1a1a;
}



</style>