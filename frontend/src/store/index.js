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
        }
    },
    mutations: {

        authUser(state) {
            state.isAuth = true
        },

    },
    actions: {},
    // plugins: [createPersistPlugin()],
})

export default store