import { createStore } from 'vuex'


const store = createStore({
    state() {
        return {
            isAuth: false,
            token: '',
            cart: {}
        }
    },
    mutations: {
        initStore(state) {

          if (localStorage.getItem('token')) {
              state.token = localStorage.getItem('token')
              state.isAuth = true
          } else {
              state.token = ''
              state.isAuth = false
          }
        },
        setCart(state, cart) {
            state.cart = cart
        },
        setToken(state, token) {
            state.token = token
            state.isAuth = true
        },
        removeToken(state) {
            state.token = ''
            state.isAuth = false
        },
    },
})

export default store