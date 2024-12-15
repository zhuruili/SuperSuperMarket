export default [
    {
      path: '/ticket',
      name: 'toBeDelivered',
      meta: {
        index: 50
      },
      component: () => import('@/views/ticket/ticket.vue')
    }
  ]