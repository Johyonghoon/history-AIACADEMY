import { PayloadAction } from "@reduxjs/toolkit";
import { call, delay, put, takeLatest } from "redux-saga/effects"
import { string } from 'yup'
import userActions from "@/modules/users"
import { currentTime } from "@/components/admin/Utils";
import { userSignUpApi } from "@/apis/userApi";
// api


interface UserSignUpType{
    type: string,
    payload: {
        user_email: string, password: string, userName: string
    }
}

interface UserSignUpSuccessType{
    type: string,
    payload: {
        user_name: string
    }
}

function* join(user: UserSignUpType){
    try{
        console.log(` ${currentTime} : userSaga 내부에서 FastAPI 넘기는 값 ${JSON.stringify(user)} `)
        //const response : UserSignUpSuccessType = yield userSignUpApi(user.payload)
        //console.log(` ${currentTime} : userSaga 내부에서 join 성공 ${JSON.stringify(response)} `)
    }catch(err){
        console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
    }
}

export function* watchSignUp(){
    yield takeLatest(userActions.actions.signUpRequest, join)
}