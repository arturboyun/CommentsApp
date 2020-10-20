<template>
  <div class="home">
    <div class="comments">
      <div class="comments__header">
        <h2>{{ commentsCount }} comments</h2>
        <Pagination :currentPage="currentPage" :totalPages="totalPages" @page-changed="pageChanged"/>
      </div>

      <div class="comments__sort">
        <div class="sort__item" :class="{ active: sortedByDate() }" @click="sort('date')">
          Date
          <img
              v-if="sortedByDate()"
              :class="{descending: sortedDirectionIsDec()}"
              src="@/assets/icons/chevron.svg" alt=""
          />
        </div>
        <div class="sort__item" :class="{ active: sortedByUsername() }" @click="sort('username')">
          User name
          <img
              v-if="sortedByUsername()"
              :class="{descending: sortedDirectionIsDec()}"
              src="@/assets/icons/chevron.svg" alt=""
          />
        </div>
        <div class="sort__item" :class="{ active: sortedByEmail() }" @click="sort('email')">
          E-mail
          <img
              v-if="sortedByEmail()"
              :class="{descending: sortedDirectionIsDec()}"
              src="@/assets/icons/chevron.svg" alt=""
          />
        </div>
      </div>

      <div class="divider"></div>

      <div class="comments__content" v-if="comments">
        <Comment
            v-for="comment in comments"
            :key="comment.id"
            :id="comment.id"
            :text="comment.text"
            :username="comment.username"
            :email="comment.email"
            :date="comment.date"
            :reply_to="comment.reply_to"
            :replies="comment.replies"
            @answer-to="answerTo"
        />
      </div>

      <div class="comments__footer">
        <Pagination :currentPage="currentPage" :totalPages="totalPages" @page-changed="pageChanged"/>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import moment from "moment"
import Comment from "@/components/Comment";
import Pagination from "@/components/Pagination";

export default {
  name: "Home",
  components: {Comment, Pagination},
  data() {
    return {
      sortBy: 'date',
      sortDirection: "-"
    }
  },
  created() {
    this.$store.dispatch('fetchComments')
  },
  computed: {
    currentPage() {
      return this.$store.getters.currentPage
    },
    totalPages() {
      return this.$store.getters.totalPages
    },
    commentsCount() {
      return this.$store.getters.commentsCount
    },
    comments() {
      return this.$store.getters.comments
    }
  },
  methods: {
    answerTo(id) {
      this.$emit("answer-to", id)
    },
    sortedByUsername() {
      return this.sortBy === 'username'
    },
    sortedByEmail() {
      return this.sortBy === 'email'
    },
    sortedByDate() {
      return this.sortBy === 'date'
    },
    sortedDirectionIsDec() {
      return this.sortDirection === '-'
    },
    pageChanged(page) {
      this.$store.dispatch('fetchComments', page)
    },
    sort(by) {
      if (by === this.sortBy) {
        if (this.sortDirection === '+')
          this.sortDirection = '-'
        else if (this.sortDirection === '-')
          this.sortDirection = '+'
      } else {
        this.sortBy = by
      }
      this.$store.dispatch('sortBy', {sortBy: this.sortBy, sortDirection: this.sortDirection})
    }
  }
}
</script>

<style lang="scss" scoped>
.home {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  width: 100%;
  min-height: 100vh;

  .comments {
    width: 100%;
    max-width: 770px;
    min-height: 100vh;
    margin: 0 8px;
    padding: 20px 0 20px 0;
    border-radius: 15px 15px 0 0;
    background-color: #ffffff;
    box-shadow: 0 25px 50px 0 rgba(0, 0, 0, 0.15);

    .comments__header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      margin: 0 0 15px 0;

      h2 {
        margin: 0;
        font-size: 24px;
        font-weight: 600;
        line-height: 24px;
      }
    }

    .comments__sort {
      padding: 0 24px;
      display: flex;

      .sort__item {
        font-size: 15px;
        font-weight: normal;
        line-height: 15px;
        margin-right: 15px;
        cursor: pointer;
        transition: 0.3s ease;

        & > img {
          transition: .5s ease;
        }

        & > img.descending {
          transform: rotate(180deg);
        }

        &.active {
          position: relative;
          color: var(--accent-color);
          font-weight: 600;

          &:after {
            content: "";
            position: absolute;
            top: 22px;
            left: 0;
            width: 100%;
            height: 3px;
            background-color: var(--accent-color);
          }
        }

        &:last-child {
          margin: 0;
        }

        &:hover {
          color: var(--accent-color);
        }
      }
    }

    .divider {
      width: 100%;
      height: 1px;
      background-color: var(--primary-color);
      margin: 10px 0 15px 0;
    }

    .comments__content {
      padding: 0 24px;
    }

    .comments__footer {
      display: flex;
      align-items: center;
      justify-content: center;
    }
  }
}
</style>
