var App = angular.module("MusicHasTheRightToChildren", []);

App.controller('MHTRTCCtrl', function($scope, $http) {
  $http.get('data/records.json')
       .then(function(res){
          $scope.records = res.data;                    
        }); 
});
