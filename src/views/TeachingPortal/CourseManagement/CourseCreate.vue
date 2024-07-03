<script setup>

import {InfoFilled, Plus, Promotion, ZoomIn} from "@element-plus/icons-vue"
import {inject, onMounted, ref} from "vue";
import {ElMessage} from "element-plus";
import {academicDiscplines} from "@/assets/static/js/resources.js";

const upload = ref();
const dialogImageUrl = ref('')
const dialogVisible = ref(false)
const handleExceed = (files)=>{
  ElMessage({
    message: '只能上传一张图片哦😣',
    type: 'warning',
    duration: 2000
  })
};
const fileList = ref([]);
const handlePictureCardPreview = async file => {
  dialogImageUrl.value = file.url;
  dialogVisible.value = true
};
const handleRemove = (file, fileList) => {
  console.log(file, fileList);
};

const courseForm= ref({
})

const rules = {
  name: [
    { required: true, message: '请输入课程名称', trigger: 'blur' },
  ],
}



const dataSource = ref([])
let id = 1
const append = (data) => {
  const newChild = { id: id++, label: '新章节', children: [] }
  if (!data.children) {
    data.children = []
  }
  data.children.push(newChild)
  dataSource.value = [...dataSource.value]
  workObject.value = dataSource.value
}
const edit = (data) => {
  data.label = chapterName.value
  chapterName.value = ''
  dataSource.value = [...dataSource.value]
  workObject.value = dataSource.value
}
const appendParent = (data) => {
  const newChild = { id: id++, label: '新章节', children: [] }
  dataSource.value.push(newChild)
  workObject.value = dataSource.value
}
const remove = (node, data) => {
  const parent = node.parent
  const children = parent.data.children || parent.data
  const index = children.findIndex((d) => d.id === data.id)
  children.splice(index, 1)
  dataSource.value = [...dataSource.value]
  workObject.value = dataSource.value
}

const chapterName = ref('')

const workObject = inject('workObject')
const workRule = inject('workRule')
onMounted(() => {
  workObject.value = dataSource.value
})

</script>

<template>
  <div class="Center-Flex" style="width: 100%">
  <div class="glowing-container" style="width: 100%; max-width: 1100px">
    <el-form
        :rules="rules"
        label-width="auto"
    >
      <div class="Space-Between-Flex">
        <div class="Center-Flex" style="flex-direction: column">
          <el-text style="margin-bottom: 12px">课程图片</el-text>
          <el-upload
              v-model:file-list="fileList"
              :limit="1"
              :auto-upload="false"
              ref="upload"
              :list-type="'picture-card'"
              :on-exceed="handleExceed"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
          >
            <el-icon><Plus /></el-icon>
          </el-upload>
        </div>
        <el-divider direction="vertical" style="height: 164px; margin-left: 24px; margin-right: 24px"/>
        <div style="width: 100%">
          <div class="Space-Between-Flex">
            <el-form-item label="课程名称" props="name" required style="flex: 1">
              <el-input v-model="courseForm.name"
                        style="max-width: 280px"
                        maxlength="30"
                        show-word-limit
                        placeholder="请在此输入课程名称"
              >
              </el-input>
            </el-form-item>
            <el-form-item label="学科分类" props="name" required style="flex: 1; width: 100%">
              <el-cascader
                  v-model="courseForm.illustration"
                  :options="academicDiscplines"
              />
            </el-form-item>
          </div>
          <el-form-item label="教学目标" props="name">
            <el-input v-model="courseForm.principle"
                      maxlength="120"
                      :autosize="{ minRows: 2, maxRows: 4 }"
                      show-word-limit
                      placeholder="请在此输入课程教学目标" type="textarea"
            >
            </el-input>
          </el-form-item>
          <el-form-item label="教学原则" props="name">
            <el-input v-model="courseForm.target"
                      maxlength="120"
                      :autosize="{ minRows: 2, maxRows: 4 }"
                      show-word-limit
                      placeholder="请在此输入课程教学原则" type="textarea"
            >
            </el-input>
          </el-form-item>
        </div>
      </div>
      <el-divider/>
      <el-form-item label="课程背景" props="name">
        <el-input v-model="courseForm.background"
                  maxlength="120"
                  :autosize="{ minRows: 2, maxRows: 4 }"
                  show-word-limit
                  placeholder="请在此输入课程背景" type="textarea"
        >
        </el-input>
      </el-form-item>
      <el-form-item label="课程介绍" props="name">
        <el-input v-model="courseForm.description"
                  maxlength="600"
                  :autosize="{ minRows: 4, maxRows: 8 }"
                  show-word-limit
                  placeholder="请在此输入课程简介" type="textarea"
        >
        </el-input>
      </el-form-item>
      <el-divider content-position="left" style="margin-top: 32px">
        <el-text>章节列表
          <el-button :icon="Plus" type="primary" size="small" style="margin-left: 12px"
                     @click="appendParent(dataSource)"
          >添加</el-button>
        </el-text>
      </el-divider>
      <div style="width: 100%; height: 240px">
        <el-scrollbar>
          <el-tree
              v-if="dataSource.length"
              :data="dataSource"
              node-key="id"
              default-expand-all
              :expand-on-click-node="false"
          >
            <template #default="{ node, data }">
            <span class="custom-tree-node">
              <span>{{ node.label }}</span>
              <span>
                <el-button @click="append(data)"
                           size="small"
                   style="color:var(--el-color-primary);"> 添加 </el-button>
                <el-popover
                    width="220"
                    :icon="InfoFilled"
                    placement="right"
                    icon-color="#626AEF"
                    trigger="click"
                >
                  <template #reference>
                     <el-button size="small"
                                @click="chapterName=data.label"
                     > 编辑 </el-button>
                  </template>
                  <el-input size="small" v-model="chapterName" placeholder="请输入章节名称" />
                    <div style="
                        margin-top: 12px;
                        display: flex;
                        justify-content: right;
                        align-content: flex-end">
                      <el-button type="danger"
                                 size="small"
                                 @click="chapterName=''">
                        取消
                      </el-button>
                       <el-button
                           @click="edit(data)"
                           :icon="Promotion" type="success" size="small">
                        确认
                      </el-button>
                    </div>
                </el-popover>

                <el-button  style="margin-left: 8px; color: var(--el-color-danger)"
                            size="small"
                            @click="remove(node, data)"> 删除 </el-button>
              </span>
            </span>
            </template>
          </el-tree>
          <el-empty v-else/>
        </el-scrollbar>
      </div>
      <div class="Center-Flex" style="width: 100%">
        <el-divider>
          <el-button :icon='Promotion' type="success">建立课程</el-button>
        </el-divider>
      </div>
    </el-form>
    <el-dialog v-model="dialogVisible">
      <div class="Center-Flex" style="width: 100%">
        <img w-full :src="dialogImageUrl" alt="Preview Image" />
      </div>
    </el-dialog>
  </div>
  </div>
</template>

<style scoped>
.custom-tree-node {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  padding-right: 8px;
}
</style>