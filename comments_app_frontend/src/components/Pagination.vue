<template>
  <div class="pagination">
    <div class="pagination__left">
      <a href="#" :class="{disabled: !hasPrev()}" @click="prevPage()">
        <img src="@/assets/icons/arrow_left.svg" alt="">
      </a>
    </div>
    <div class="pagination__mid">
      <ul>
        <li v-if="hasFirst()"><a href="#" @click="changePage(1)">1</a></li>
        <li v-if="hasFirst()">...</li>
        <li v-for="page in pages" :key="page">
          <a href="#" @click="changePage(page)" :class="{ current: page === currentPage}">{{ page }}</a>
        </li>
        <li v-if="hasLast()">...</li>
        <li v-if="hasLast()"><a href="#" @click="changePage(totalPages)">{{ totalPages }}</a></li>
      </ul>
    </div>
    <div class="pagination__right">
      <a href="#" :class="{disabled: !hasNext()}" @click="nextPage()">
        <img src="@/assets/icons/arrow_right.svg" alt="">
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    currentPage: {
      type: Number,
      default: 1
    },
    totalPages: {
      type: Number,
      default: 1
    },
    pageRange: {
      type: Number,
      default: 2,
    }
  },
  computed: {
    pages() {
      const pages = []

      for (let i = this.rangeStart; i <= this.rangeEnd; i++) {
        pages.push(i)
      }

      return pages
    },
    rangeStart() {
      const start = this.currentPage - this.pageRange
      return (start > 0) ? start : 1
    },
    rangeEnd() {
      const end = this.currentPage + this.pageRange
      return (end < this.totalPages) ? end : this.totalPages
    },
    prevPageNum() {
      return this.currentPage - 1
    },
    nextPageNum() {
      return this.currentPage + 1
    },
  },
  methods: {
    hasFirst() {
      return this.rangeStart !== 1
    },
    hasLast() {
      return this.rangeEnd < this.totalPages
    },
    hasPrev() {
      return this.$store.state.hasPrevPage
    },
    hasNext() {
      return this.$store.state.hasNextPage
    },
    prevPage() {
      if (this.hasPrev())
        this.changePage(this.prevPageNum)
    },
    nextPage() {
      if (this.hasNext())
        this.changePage(this.nextPageNum)
    },
    changePage(page) {
      this.$emit('page-changed', page)
    }
  }
}
</script>

<style lang="scss" scoped>
.pagination {
  display: flex;
  align-items: center;
  justify-content: space-between;

  .pagination__left > a, .pagination__right > a {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: var(--accent-color);
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    border-radius: 50%;
    width: 26px;
    height: 26px;
  }

  .pagination__left {
    margin-right: 12px;
  }

  .pagination__mid {
    margin-right: 12px;

    ul {
      display: flex;
      align-items: center;
      justify-content: center;
      list-style: none;
      margin: 0;
      padding: 0;

      li {
        margin-right: 8px;

        &:last-child {
          margin-right: 0;
        }

        a {
          display: flex;
          align-items: center;
          justify-content: center;
          width: 24px;
          height: 24px;
          border-radius: 50%;
          transition: .3s ease;

          &:last-child {
            margin-right: 0;
          }

          &:hover {
            color: var(--black-color);
            background-color: #eaf5ff;
          }

          &.current {
            cursor: default;
            border: 1px solid var(--accent-color);
          }
        }
      }
    }
  }

  a.disabled {
    cursor: default;
    background-color: var(--grey-color);
  }
}
</style>