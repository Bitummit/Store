import { createStore } from 'vuex'


const store = createStore({
    state() {
        return {
            isAuth: false,
            token: '',
            cart: {
                items: [],
            }
        }
    },
    mutations: {
        initStore(state) {
          if (localStorage.getItem('cart')) {
              state.cart = JSON.parse(localStorage.getItem('cart'))
          }  else {
              localStorage.setItem('cart', JSON.stringify(state.cart))
          }

          if (localStorage.getItem('token')) {
              state.token = localStorage.getItem('token')
              state.isAuth = true
          } else {
              state.token = ''
              state.isAuth = false
          }
        },
        setToken(state, token) {
            state.token = token
            state.isAuth = true
        },
        removeToken(state) {
            state.token = ''
            state.isAuth = false
        },
        addToCart(state, item) {
            // const exists = state.cart.items.filter(i => i.item.id === item.item.id)
            //
            // if (exists.length) {
            //     exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
            // } else {
                state.cart.items.push(item)
            // }
            localStorage.setItem('cart', JSON.stringify(state.cart))
        }
    },
})

export default store