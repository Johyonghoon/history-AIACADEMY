import { createSlice, PayloadAction } from "@reduxjs/toolkit"
export interface IuserType{
    user_id: string
    user_email: string
    password: string
    user_name: string
    phone: string
    birth: string
    address: string
    job: string
    user_interests: string
    token: string
    create_at: string
    updated_at: string
}

export interface IUserState{
    data: IuserType[]
    status: 'idle' | 'loading' | 'failed'
}
const initialState: IUserState = {
    data: [],
    status: 'idle'
}
const userSlice = createSlice({
    name: 'userSlice',
    initialState,
    reducers: {
        signUpRequest(state: IUserState, _payload){
            state.status = 'loading'
        },
        signUpSuccess(state: IUserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        signUpFailed(state: IUserState, {payload}){
            state.status = 'failed'
        },
        loginRequest(state: IUserState, _payload){
            state.status = 'loading'
        },
        loginSuccess(state: IUserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        loginFailed(state: IUserState, {payload}){
            state.status = 'failed'
        }
    }
})

export const {
    signUpRequest, signUpSuccess, signUpFailed,
    loginRequest, loginSuccess, loginFailed
} = userSlice.actions
export default userSlice