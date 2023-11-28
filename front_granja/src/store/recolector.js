import {createSlice, createAsyncThunk} from '@reduxjs/toolkit';
import Axios from 'axios';
import apiConfig from '../config/api';

export const signUp = createAsyncThunk('recolector/singUp', async (credential)=>{
    //operacion asincrona
    let response = await Axios.post(`${apiConfig.domain}/recolector/v1/api`,{
        credential
    })
    console.log(response.body);
    return response.body
});

let recolectorSlice = createSlice({
    name: 'recolector',
    initialState: {
        name: null,
        status: ''
    },
    reducers:{
        signIn: (state, accion) =>{
            state.name = accion.payload;
        },
        logOut: (state)=>{
            state.name= null;
        }
    },
    extraReducers:{
        [signUp.pending]: (state, action) =>{
            state.status='loading.....'
        },
        [signUp.fulfilled]: (state, action) =>{
            state.name=action.payload
            state.status='fullfilled'
        },
        [signUp.rejected]: (state, action) =>{
            state.status='fallo'
        }
    }
});

export const {signIn, logOut}=recolectorSlice.actions;

export default recolectorSlice.reducer;