<template>
  <div class="login_box">
    <el-row>
      <el-col :span="8">
        <h2 class="login_box_title">运维管理系统</h2>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="8">
        <el-input id="name" v-model="name" placeholder="请输入帐号">
          <template slot="prepend">帐号</template>
        </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="8">
        <el-input id="password" v-model="password" type="password" placeholder="请输入密码">
          <template slot="prepend">密码</template>
        </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="8">
        <el-button id="login" v-on:click="loginIn" style="width:100%" type="primary">登录</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      name: '',
      password: ''
    }
  },
  methods: {
    loginIn: function (event) {
      var that = this
      var name = that.name
      var password = that.password
      console.log(name, password)
      this.$message = function (param) {
      }
      if (name === '' && password === '') {
        this.$message({
          message: '请输入账号密码！',
          type: 'error'
        })
        return
      } else if (name !== '' && password === '') {
        this.$message({
          message: '请输入密码！',
          type: 'error'
        })
        return
      } else if (name === '' && password !== '') {
        this.$message({
          message: '请输入用户名！',
          type: 'error'
        })
        return
      }
      $.ajax = function (param) {
      }
      $.ajax({
        type: 'get',
        url: '',
        async: true,
        data: {
          name: name,
          password: password
        }})
    }
  }
}
</script>

<style>
  .login_box {
    margin-top: 16%;
    margin-left: 40%;
  }
  .login_box .el-row {
    margin-bottom: 20px;
  }
  .login_box_title{
    text-align: center;
  }
</style>
