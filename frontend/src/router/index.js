import {createRouter, createWebHistory} from 'vue-router'
import Catalog from '../views/CatalogView.vue'
import Category from '../views/CategoryView.vue'
import Cart from '../views/CartView.vue'
import MyAccount from '../views/MyAccountView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'catalog',
            component: Catalog
        },
        {
            path: '/:category',
            name: 'view_by_category',
            props: true,
            component: Category
        },
        {
            path: '/detail/:name',
            name: 'detail-item-view',
            props: true,
            component: () => import('../views/DetailItemView.vue')
        },
        {
            path: '/cart',
            name: 'cart',
            component: Cart
        },
        {
            path: '/account',
            name: 'account',
            component: MyAccount
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue')
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('../views/RegisterView.vue')
        },

    ]
})

export default router
