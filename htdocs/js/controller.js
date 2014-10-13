
var app = angular.module("MusicHasTheRightToChildren", []);

app.controller("PostsCtrl", function($scope, $http) {
  $http.get('data/records.json').
    success(function(data, status, headers, config) {
      $scope.posts = data;
    }).
    error(function(data, status, headers, config) {
      // log error
    });
});


