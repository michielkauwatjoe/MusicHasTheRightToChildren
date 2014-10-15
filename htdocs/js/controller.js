var App = angular.module("MusicHasTheRightToChildren", []);

App.controller('MHTRTCCtrl', function($scope, $http) {
  $http.get('data/discogs.json')
       .then(function(res){
          $scope.discogs = res.data;                    
        }); 
});
