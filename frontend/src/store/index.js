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
    actions: {},
    // plugins: [createPersistPlugin()],
})

export default store