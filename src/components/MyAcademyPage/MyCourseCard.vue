<script setup lang="ts">
import router from "@/router";

const props = defineProps({
  brief: {
    type: Object,
    required: true
  },
})

</script>
<template>
  <el-card id="course-card">
    <div class="Space-Between-Flex">
      <img
          src="@/assets/static/img/course/1/course.jpg"
          id="course-image" alt=""/>

      <div id="info-container">
        <div class="Space-Between-Flex"
             style="margin-bottom: 32px"
        >
          <h2>{{props.brief.name}}</h2>
          <div>
            <el-tag
                id="intelligent-tag"
                effect="plain"
                style="margin-right: 16px"
            >
              AI助学 | 智能课
            </el-tag>
            <el-tag
                id="featured-tag"
                effect="plain"
            >
              AI赋能 | 精选课
            </el-tag>
          </div>
        </div>

        <div class="Space-Between-Flex">
          <div id="description-container">
            <el-text class="description-text">
              {{ props.brief.description }}
            </el-text>
            <el-text class="description-text">
              {{ props.brief.illustration }}
            </el-text>
          </div>
          <el-button type="primary" style="width: 128px" @click="router.push('academy/my-course/' + props.brief.id)">去学习</el-button>
        </div>

      </div>

    </div>
  </el-card>
</template>

<style scoped>
#course-image{
  height: 128px;
  border-radius: 8px;
  margin-right: 24px;
}
#info-container{
  width: 100%;
  height: 100%;
}

#description-container{
  display: flex;
  justify-content: flex-start;
  text-align: left;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
.description-text{
  width: 100%;
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


#featured-tag{
  padding: 12px;
  transition: 0.5s;
  border: var(--color-featured) 1px solid;
  color: var(--color-featured)
}

#featured-tag:hover{
  box-shadow: var(--color-featured) 0 0 8px;
}

#intelligent-tag{
  padding: 12px;
  transition: 0.5s;
  border: var(--color-intelligent) 1px solid;
  color: var(--color-intelligent)
}

#intelligent-tag:hover{
  box-shadow: var(--color-intelligent) 0 0 8px;
}


</style>