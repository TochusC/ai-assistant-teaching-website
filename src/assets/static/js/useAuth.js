import { ref, computed } from 'vue';
import { useStorage } from '@vueuse/core';

export function useAuth() {
    const isAuthenticated = ref(false);
    const user = ref(null);
    const storage = useStorage('user');

    const login = (userData) => {
        isAuthenticated.value = true;
        user.value = userData;
        storage.value = JSON.stringify(userData); // 将用户信息存储到本地
    };

    const logout = () => {
        isAuthenticated.value = false;
        user.value = null;
        storage.value = null; // 清除本地存储的用户信息
    };

    // 检查本地存储中是否有用户信息，如果有则自动登录
    if (storage.value != null && storage.value !== 'null' && storage.value !== 'undefined') {
        isAuthenticated.value = true;
        user.value = JSON.parse(storage.value);
    }

    // 派生其他状态
    const isAdmin =
        computed(() => user.value && user.value.role === 'admin');

    return {
        isAuthenticated,
        user,
        login,
        logout,
        isAdmin,
    };
}
