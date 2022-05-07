/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { UserList } from '../models/UserList';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class UsersService {

    /**
     * @returns UserList
     * @throws ApiError
     */
    public static usersList(): CancelablePromise<Array<UserList>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/users/',
        });
    }

}