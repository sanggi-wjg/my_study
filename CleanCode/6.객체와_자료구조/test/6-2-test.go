package test

import (
	"bytes"
	"io/ioutil"
	"net/http"
)

type HttpSuccessResult struct {
	statusCode int
	status     string
	result     string
}

func NewHttpSuccessResult(statusCode int, status string, result string) *HttpSuccessResult {
	h := HttpSuccessResult{
		statusCode: statusCode,
		status:     status,
		result:     result,
	}
	return &h
}

func (h *HttpSuccessResult) StatusCode () int{
	return h.statusCode
}

func (h *HttpSuccessResult) Status () int{
	return h.status
}
func (h *HttpSuccessResult) Result () int{
	return h.result
}

func main() {
	reqBody := bytes.NewBufferString("Post plain text")
	resp, err := http.Post("http://sample.post", "text/plain", reqBody)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	respBody, err := ioutil.ReadAll(resp.Body)
	if err == nil {
		status := resp.Status
		statusCode := resp.StatusCode
		result := string(respBody)
		httpSuccessResult := NewHttpSuccessResult(statusCode, status, result)
	}
	else{
		htttpFailedResult := ...
	}
}
