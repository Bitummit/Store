import { createStore } from 'vuex'

// const createPersistPlugin = () => {
//     return (store) => {
//         store.subscribe(mutation => {
//             localStorage.setItem(`time`, JSON.stringify(store.state.time))
//
//         })
//     }
// }

const store = createStore({
    state() {
        return {
            isAuth: false,
            token: '',
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
        setToken(state, token) {
            state.token = token
            state.isAuth = true
        },
        removeToken(state) {
            state.token = ''
            state.isAuth = false
        }
    },
    actions: {},
    // plugins: [createPersistPlugin()],
})

export default store