export default [
    {
      path: '/ticket',
      name: 'getTicket',
      meta: {
        index: 50
      },
      component: () => import('@/views/ticket/ticket.vue')
    }
  ]