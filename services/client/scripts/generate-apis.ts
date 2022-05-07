import { generate } from "openapi-typescript-codegen";
import axios from "axios";
import fs from "fs";

axios({
  url: `${process.env.BASE_API_URL}/api/v1/schema/`,
  method: "GET",
  responseType: "stream",
})
  .then(async (response) => {
    response.data.pipe(fs.createWriteStream("openapi.yaml"));
    await generate({
      input: "./openapi.yaml",
      output: "./apis",
      httpClient: "axios",
    });
    console.info("API 생성이 완료됐습니다.")
  })
  .catch((error) => {
    console.error(error.code);
  });
