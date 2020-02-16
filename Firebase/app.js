(function() {


	const config = {
		apiKey: "AIzaSyB0ksX_foPQcuGXiDSbeUQ0JEXnDa9KhVU",
	    authDomain: "uccjk2019-e447e.firebaseapp.com",
	    databaseURL: "https://uccjk2019-e447e.firebaseio.com",
	    projectId: "uccjk2019-e447e",
	    storageBucket: "uccjk2019-e447e.appspot.com",
	    messagingSenderId: "643715142169",
	    appId: "1:643715142169:web:552682c64c3323ab101088",
	    measurementId: "G-KKJ8YVZGYR"
	};
	firebase.initializeApp(config);


	const txtEmail = document.getElementById('txtEmail');
	const txtPassword = document.getElementById('txtPassword');
	const btnLogin = document.getElementById('btnLogin');
	const btnLSignup = document.getElementById('btnSignup');
	const btnLogout = document.getElementById('btnLogout');


	btnLogin.addEventListener('click', e => {

		const email = txtEmail.value;
		const pass = txtPassword.value;
		const auth = firebase.auth();

		const promise = auth.signInWithEmailAndPassword(email, pass);
		promise.catch(e => window.alert("User Does Not Exist"))
	});

	btnSignup.addEventListener('click', e => {

		const email = txtEmail.value;
		const pass = txtPassword.value;
		const auth = firebase.auth();

		const promise = auth.createUserWithEmailAndPassword(email, pass);
		promise.catch(e => window.alert("User Already Exists"))

	});

	btnLogout.addEventListener('click', e => {
		firebase.auth().signOut();
	});

	firebase.auth().onAuthStateChanged(firebaseUser => {
		if(firebaseUser) {
			console.log(firebaseUser);
		} else {
			console.log('not logged in');
		}

	});

}());