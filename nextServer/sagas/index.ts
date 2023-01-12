import { all, fork } from "redux-saga/effects"
import{ watchSignUp } from "./userSaga"

export default function* rootSaga(){
    yield all([
        fork(watchSignUp)
    ])
}