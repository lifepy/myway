		function updateTips( t ) {
			$('.validateTips')
				.text( t )
				.addClass( "ui-state-highlight" );
			setTimeout(function() {
				$('.validateTips').removeClass( "ui-state-highlight", 1500 );
			}, 500 );
		}

		function checkLength( o, n, min, max ) {
			if ( o.val().length > max || o.val().length < min ) {
				o.addClass( "ui-state-error" );				
				updateTips( "Length of " + n + " must be between " +
					min + " and " + max + "." ); 
				return false;
			} else {
				return true;
			}
		}

		function checkRegexp( o, regexp, n ) {
			if ( !( regexp.test( o.val() ) ) ) {
				o.addClass( "ui-state-error" );
				updateTips( n );
				return false;
			} else {
				return true;
			}
		}
		
		function checkRetype( o1,o2) {
			if ( !(o1.val()==o2.val()) ) {
				o2.addClass( "ui-state-error" );
				updateTips( "Retyped password is not consistant with the password!" );
				return false;
			} else {
				return true;
			}
		}
