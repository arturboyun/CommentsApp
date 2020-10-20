<template>
  <div class="comment" :class="{ reply: isReply}">

    <div class="comment__info">

      <div class="info__left">
        <div class="info__username">{{ username }}</div>
        <div class="info__email">{{ email }}</div>
      </div>

      <div class="info__right">
        <div class="info__date">{{ getDate }}</div>
      </div>

    </div>

    <div class="comment__text">{{ text }}</div>

    <a href="#" class="comment__answer" @click="answerTo(id)">Ответить</a>

    <div v-if="haveReplies" class="replies">
      <Comment
          v-for="reply in replies"
          :key="reply.id"
          :id="reply.id"
          :text="reply.text"
          :username="reply.username"
          :email="reply.email"
          :date="reply.date"
          :reply_to="reply.reply_to"
          :replies="reply.replies"
          @answer-to="answerTo"
      />
    </div>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: "Comment",
  props: {
    'id': Number,
    'text': String,
    'username': String,
    'email': String,
    'date': Date,
    'reply_to': Number,
    'replies': Array
  },
  computed: {
    getDate() {
      return moment(this.date).format("DD.MM.YYYY H:m")
    },
    isReply() {
      return !!this.reply_to
    },
    haveReplies() {
      return this.replies.length > 0
    }
  },
  methods: {
    answerTo(id) {
      // console.log(this.id, this.username, this.text, id)
      this.$emit("answer-to", id)
    }
  }
}
</script>

<style lang="scss" scoped>
.comment {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  flex-direction: column;
  margin-bottom: 20px;

  .comment__info {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    width: 100%;

    .info__username {
      font-weight: bold;
      margin-bottom: 5px;
    }

    .info__email, .info__date {
      font-size: 12px;
      line-height: 12px;
      color: var(--grey-color);
      margin-bottom: 5px;
    }

    .info__right {
      text-align: end;
    }
  }

  .comment__text {
    font-size: 15px;
    line-height: 15px;
    word-break: break-all;
    margin-bottom: 5px;
  }
}

.comment .reply {
  padding-left: 16px;
  margin-top: 10px;
  margin-bottom: 0;
}

.comment > .replies {
  width: 100%;
  margin-top: 10px;
  margin-bottom: 0;
  border-left: 1px dashed var(--grey-color);
}
</style>