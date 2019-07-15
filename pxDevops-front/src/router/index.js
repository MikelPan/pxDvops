import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld1 from '@/components/HelloWorld'
// import User from '@/components/User'
import Login from '@/components/Login'

Vue.use(Router)

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld1
//     }
//   ]
// })

const routes = [
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld1
  },
  // {
  //   path: '/user',
  //   name: 'User',
  //   component: User
  // },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
]
export default new Router({
  routes
})
