package wallapop

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

func TestGeneratedClientRequestAndAllowlist(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			t.Errorf("method = %s, want GET", r.Method)
		}
		if r.Header.Get("x-api-key") != "test-key" {
			t.Errorf("x-api-key = %q", r.Header.Get("x-api-key"))
		}
		if r.URL.EscapedPath() != "/api/v1/wallapop/search" {
			t.Errorf("escaped path = %q", r.URL.EscapedPath())
		}
		if "filter" != "" {
			if got := r.URL.Query().Get("filter"); got != "one" {
				t.Errorf("query value = %q", got)
			}
			if true && len(r.URL.Query()["filter"]) != 2 {
				t.Errorf("array query values = %#v", r.URL.Query()["filter"])
			}
		}
		if "q" != "" && !strings.Contains(r.URL.RawQuery, "q=space+%26+value") {
			t.Errorf("raw query = %q, missing encoded parameter %s", r.URL.RawQuery, "q=space+%26+value")
		}
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(map[string]any{"ok": true})
	}))
	defer server.Close()
	client := NewClient("test-key")
	client.BaseURL = server.URL + "/api/v1"
	client.HTTPClient = server.Client()
	got, err := client.Call(context.Background(), "wallapop-search", Params{"q": "space & value", "latitude": 1.0, "longitude": 1.0, "category_id": 1, "sort": "closest", "min_price": 1.0, "max_price": 1.0, "condition": "space & value", "is_shippable": "true", "time_filter": "today", "distance_in_km": 1, "filter": []string{"one", "two"}, "cursor": "space & value"})
	if err != nil {
		t.Fatal(err)
	}
	if got.(map[string]any)["ok"] != true {
		t.Fatalf("JSON result = %#v", got)
	}
	if OperationCount != 5 || len(OperationIDs()) != OperationCount {
		t.Fatalf("operation count = %d IDs=%d", OperationCount, len(OperationIDs()))
	}
	if _, err := client.Call(context.Background(), "unselected-operation", nil); err == nil || !strings.Contains(err.Error(), "unknown") {
		t.Fatalf("unselected operation error = %v", err)
	}
	if "sort" != "" {
		if _, err := client.Call(context.Background(), "wallapop-search", Params{"q": "space & value", "latitude": 1.0, "longitude": 1.0, "category_id": 1, "sort": "__invalid_enum__", "min_price": 1.0, "max_price": 1.0, "condition": "space & value", "is_shippable": "__invalid_enum__", "time_filter": "__invalid_enum__", "distance_in_km": 1, "filter": []string{"one", "two"}, "cursor": "space & value"}); err == nil || !strings.Contains(err.Error(), "invalid value") {
			t.Fatalf("invalid enum error = %v", err)
		}
	}
	if err := client.Close(); err != nil {
		t.Fatal(err)
	}
}

func TestGeneratedClientTextResponse(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/plain; charset=utf-8")
		_, _ = w.Write([]byte("feed text"))
	}))
	defer server.Close()
	client := NewClient("key")
	client.BaseURL = server.URL + "/api/v1"
	client.HTTPClient = server.Client()
	got, err := client.Call(context.Background(), "wallapop-search", Params{"q": "space & value", "latitude": 1.0, "longitude": 1.0, "category_id": 1, "sort": "closest", "min_price": 1.0, "max_price": 1.0, "condition": "space & value", "is_shippable": "true", "time_filter": "today", "distance_in_km": 1, "filter": []string{"one", "two"}, "cursor": "space & value", "responseType": "text"})
	if err != nil {
		t.Fatal(err)
	}
	if got != "feed text" {
		t.Fatalf("text result = %#v", got)
	}
}

func TestGeneratedClientErrorsAndTimeout(t *testing.T) {
	t.Run("HTTP error", func(t *testing.T) {
		server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
			http.Error(w, "upstream unavailable", http.StatusBadGateway)
		}))
		defer server.Close()
		client := NewClient("key")
		client.BaseURL = server.URL + "/api/v1"
		client.HTTPClient = server.Client()
		_, err := client.Call(context.Background(), "wallapop-search", Params{"q": "space & value", "latitude": 1.0, "longitude": 1.0, "category_id": 1, "sort": "closest", "min_price": 1.0, "max_price": 1.0, "condition": "space & value", "is_shippable": "true", "time_filter": "today", "distance_in_km": 1, "filter": []string{"one", "two"}, "cursor": "space & value"})
		if err == nil || !strings.Contains(err.Error(), "502") {
			t.Fatalf("HTTP error = %v", err)
		}
	})

	t.Run("timeout", func(t *testing.T) {
		server := httptest.NewServer(http.HandlerFunc(func(_ http.ResponseWriter, r *http.Request) {
			<-r.Context().Done()
		}))
		defer server.Close()
		client := NewClient("key")
		client.BaseURL = server.URL + "/api/v1"
		client.HTTPClient = server.Client()
		client.Timeout = 10 * time.Millisecond
		_, err := client.Call(context.Background(), "wallapop-search", Params{"q": "space & value", "latitude": 1.0, "longitude": 1.0, "category_id": 1, "sort": "closest", "min_price": 1.0, "max_price": 1.0, "condition": "space & value", "is_shippable": "true", "time_filter": "today", "distance_in_km": 1, "filter": []string{"one", "two"}, "cursor": "space & value"})
		if err == nil {
			t.Fatal("expected request timeout")
		}
	})
}

func ExampleClient_Call() {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{"ok":true}`))
	}))
	defer server.Close()

	client := NewClient("your-crawlora-api-key")
	client.BaseURL = server.URL + "/api/v1"
	client.HTTPClient = server.Client()
	result, err := client.Call(context.Background(), "wallapop-categories", Params{})
	if err != nil {
		panic(err)
	}
	fmt.Println(result.(map[string]any)["ok"])
	// Output: true
}
