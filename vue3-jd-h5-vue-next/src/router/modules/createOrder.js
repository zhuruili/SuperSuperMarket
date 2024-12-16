export default [
    {
      path: '/createOrder',
      name: 'createOrder',
      meta: {
        index: 2
      },
      component: () => import('@/views/order/createOrder.vue')
    }
  ]