import {configureStore} from '@reduxjs/toolkit';

import recolectorSlice from './recolector';

export const store = configureStore({
    reducer:{
        name: recolectorSlice
    }
})