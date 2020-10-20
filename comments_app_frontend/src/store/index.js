import Vue from 'vue'
import Vuex from 'vuex'
import {API} from "@/API";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    comments: [],
    currentPage: 1,
    totalComments: 0,
    totalPages: 1,
    hasNextPage: false,
    hasPrevPage: false,
    ordering: '-created_at'
  },
  getters: {
    comments(state) {
      return state.comments
    },
    commentsCount(state) {
      return state.comments.length
    },
    currentPage(state) {
      return state.currentPage
    },
    totalPages(state) {
      return state.totalPages
    },
  },
  mutations: {
    setComments(state, comments) {
      state.comments = comments
    },
    setCurrentPage(state, currentPage) {
      state.currentPage = currentPage
    },
    setHasNextPage(state, hasNextPage) {
      state.hasNextPage = hasNextPage
    },
    setHasPrevPage(state, hasPrevPage) {
      state.hasPrevPage = hasPrevPage
    },
    setTotalPages(state, totalPages) {
      state.totalPages = totalPages
    },
    setTotalComments(state, totalComments) {
      state.totalComments = totalComments
    },
    setOrdering(state, ordering) {
      state.ordering = ordering
    },
    setFilter(state, filter) {
      state.filter = filter
    }
  },
  actions: {
    async sortBy({ dispatch, commit }, {sortBy, sortDirection}) {
      if (sortDirection === "+")
        sortDirection = ''
      if (sortBy === 'date')
        sortBy = 'created_at'
      commit('setOrdering', sortDirection + sortBy)
      dispatch('fetchComments')
    },
    async createComment({ dispatch }, data) {
      try{
        const res = await API.post('api/v1/comments/', data)
        if (res.status === 201) {
          dispatch('fetchComments')
          return true
        }
        else
          return false
      } catch (e) {
        console.log(e)
      }
    },
    async getComment({dispatch}, id) {
      try{
        console.log(id)
        const res = await API.get(`api/v1/comments/${id}`)
        if (res.status === 200) {
          dispatch('fetchComments')
          return res.data
        }
        else
          return null
      } catch (e) {
        console.log(e)
      }
    },
    async fetchComments({commit, state}, page) {
      try {
        if (!page) page = state.currentPage
        let url = `/api/v1/comments/`
        let params = {
          page,
          ordering: state.ordering,
        }
        const result = await API.get(url, {params});
        console.log(result)
        commit('setComments', result.data.results)
        commit('setCurrentPage', page)
        commit('setHasNextPage', !!result.data.next)
        commit('setHasPrevPage', !!result.data.previous)
        commit('setTotalPages', result.data.total_pages)
        commit('setTotalComments', result.data.count)
      } catch (e) {
        console.log(e);
      }
    },
  }
})
