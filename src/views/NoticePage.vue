<script setup>
import {useAuth} from "@/assets/static/js/useAuth.js";

const {user} = useAuth()
import BlankPage from "@/views/BlankPage.vue";
import {onMounted, ref} from "vue";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import NoticeCard from "@/components/NoticePage/NoticeCard.vue";

const notice = ref([])
const fetchNotice = () => {
  axios.get(backendUrl + user.value.role + '/message/' + user.value.ident).then(res => {
    notice.value = res.data
    console.log(notice.value)
  }).catch(err => {
    console.log(err)
  })
}
const deleteMessage = (id) => {
  notice.value = notice.value.filter(item => item.id !== id)
}


onMounted(() => {
  fetchNotice()
})
</script>

<template>
  <BlankPage>
    <template #default>
      <NoticeCard v-for="message in notice" :message="message" :deleteMessage="deleteMessage"/>
    </template>
  </BlankPage>
</template>
<style scoped>

</style>