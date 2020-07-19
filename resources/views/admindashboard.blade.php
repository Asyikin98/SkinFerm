<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Admin Dashboard</title>
    <!-- plugins:css -->
    <link rel="stylesheet" href="../public/PurpleAdmin-Free-Admin-Template-master/assets/vendors/mdi/css/materialdesignicons.min.css">
    <link rel="stylesheet" href="../public/PurpleAdmin-Free-Admin-Template-master/assets/vendors/css/vendor.bundle.base.css">
    <!-- endinject -->
    <!-- Plugin css for this page -->
    <!-- End plugin css for this page -->
    <!-- inject:css -->
    <!-- endinject -->
    <!-- Layout styles -->
    <link rel="stylesheet" href="../resources/sass/dashboard.css" type="text/css">
    <!-- End layout styles -->
    <link rel="shortcut icon" href="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/favicon1.ico" />
  </head>
  <body>
    <div class="container-scroller">
      <!-- partial:partials/_navbar.html -->
      <nav class="navbar default-layout-navbar col-lg-12 col-12 p-0 fixed-top d-flex flex-row">
        <div class="text-center navbar-brand-wrapper d-flex align-items-center justify-content-center">
        </div>
        <div class="navbar-menu-wrapper d-flex align-items-stretch">
          <button class="navbar-toggler navbar-toggler align-self-center" type="button" data-toggle="minimize">
            <span class="mdi mdi-menu"></span>
          </button>
          <div class="search-field d-none d-md-block">
            <form class="d-flex align-items-center h-100" action="#">
              <div class="input-group">
                <div class="input-group-prepend bg-transparent">
                  <i class="input-group-text border-0 mdi mdi-magnify"></i>
                </div>
                <input type="text" class="form-control bg-transparent border-0" placeholder="Search">
              </div>
            </form>
          </div>

          <ul class="navbar-nav navbar-nav-right">
            <li class="nav-item nav-profile dropdown">
              <a class="nav-link dropdown-toggle" id="profileDropdown" href="#" data-toggle="dropdown" aria-expanded="false">
                <div class="nav-profile-img">
                  <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/faces/admin.png" alt="image">
                  <span class="availability-status online"></span>
                </div>
                <div class="nav-profile-text">
                  <p class="mb-1 text-black">Admin</p>
                </div>
              </a>
              <div class="dropdown-menu navbar-dropdown" aria-labelledby="profileDropdown">
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="http://localhost/fyp/fyp/public/welcome">
                  <i class="mdi mdi-logout mr-2 text-primary"></i> Signout </a>
              </div>
            </li>
            <li class="nav-item d-none d-lg-block full-screen-link">
              <a class="nav-link">
                <i class="mdi mdi-fullscreen" id="fullscreen-button"></i>
              </a>
            </li>
            <li class="nav-item nav-logout d-none d-lg-block">
              <a class="nav-link" href="http://localhost/fyp/fyp/public/welcome">
                <i class="mdi mdi-power"></i>
              </a>
            </li>
          </ul>
          <button class="navbar-toggler navbar-toggler-right d-lg-none align-self-center" type="button" data-toggle="offcanvas">
            <span class="mdi mdi-menu"></span>
          </button>
        </div>
      </nav>
      <!-- partial -->
      <div class="container-fluid page-body-wrapper">
        <!-- partial:partials/_sidebar.html -->
        <nav class="sidebar sidebar-offcanvas" id="sidebar">
          <ul class="nav">
            <li class="nav-item nav-profile">
              <a href="#" class="nav-link">
                <div class="nav-profile-image">
                  <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/faces/admin.png" alt="profile">
                  <span class="login-status online"></span>
                  <!--change to offline or busy as needed-->
                </div>
                <div class="nav-profile-text d-flex flex-column">
                  <span class="font-weight-bold mb-2">Admin</span>
                </div>
                <i class="mdi mdi-bookmark-check text-success nav-profile-badge"></i>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/fyp/fyp/public/admindashboard">
                <span class="menu-title">Dashboard</span>
                <i class="mdi mdi-home menu-icon"></i>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/fyp/fyp/public/adminuser">
                <span class="menu-title">Users</span>
                <i class="mdi mdi-account-circle menu-icon"></i>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/fyp/fyp/public/adminskintype">
                <span class="menu-title">Skin Type</span>
                <i class="mdi mdi-spray menu-icon"></i>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/fyp/fyp/public/adminroutine">
                <span class="menu-title">Skincare Routine</span>
                <i class="mdi mdi-table-large menu-icon"></i>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/fyp/fyp/public/admintips">
                <span class="menu-title">Tips</span>
                <i class="mdi mdi-table-large menu-icon"></i>
              </a>
            </li>

          </ul>
        </nav>
        <!-- partial -->
        <div class="main-panel">
          <div class="content-wrapper">
            <div class="page-header">
              <h3 class="page-title">
                <span class="page-title-icon bg-gradient-primary text-white mr-2">
                  <i class="mdi mdi-home"></i>
                </span> Dashboard </h3>
              <nav aria-label="breadcrumb">
                <ul class="breadcrumb">
                  <li class="breadcrumb-item active" aria-current="page">
                    <span></span>Overview <i class="mdi mdi-alert-circle-outline icon-sm text-primary align-middle"></i>
                  </li>
                </ul>
              </nav>
            </div>
            <div class="row">
              <div class="col-md-4 stretch-card grid-margin">
                <div class="card bg-gradient-danger card-img-holder text-white">
                  <div class="card-body">
                    <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/dashboard/circle.svg" class="card-img-absolute" alt="circle-image" />
                    <h4 class="font-weight-normal mb-3" style="background-color:black;">Total Register Users <i class="mdi mdi-account-circle mdi-24px float-right"></i>
                    </h4>
                    <h2 class="mb-5" style="color:black";>
                      <?php
                      $conn = mysqli_connect("localhost","root","","testing");
                      $query = "SELECT id FROM users ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<h3> $row </h3>";
                      ?>
                    </h2>
                  </div>
                </div>
              </div>
              <div class="col-md-4 stretch-card grid-margin">
                <div class="card bg-gradient-info card-img-holder text-white">
                  <div class="card-body">
                    <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/dashboard/circle.svg" class="card-img-absolute" alt="circle-image" />
                    <h4 class="font-weight-normal mb-3" style="background-color:black;">Total Cleanser <i class="mdi mdi-invert-colors mdi-24px float-right"></i>
                    </h4>
                    <h2 class="mb-5" style="color:black";>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM comcleanser ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Combination : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM drycleanser ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Dry : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM norcleanser ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Normal : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM oilycleanser ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Oily : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM sencleanser ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Sensitive : $row </p>";
                      ?>
                    </h2>
                  </div>
                </div>
              </div>
              <div class="col-md-4 stretch-card grid-margin">
                <div class="card bg-gradient-success card-img-holder text-white">
                  <div class="card-body">
                    <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/dashboard/circle.svg" class="card-img-absolute" alt="circle-image" />
                    <h4 class="font-weight-normal mb-3" style="background-color:black;">Total Toner <i class="mdi mdi-battery-outline mdi-24px float-right"></i>
                    </h4>
                    <h2 class="mb-5" style="color:black";>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM comtoner ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Combination : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM drytoner ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Dry : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM nortoner ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Normal : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM oilytoner ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Oily : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM sentoner ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Sensitive : $row </p>";
                      ?>
                    </h2>
                  </div>
                </div>
              </div>
              <div class="col-md-4 stretch-card grid-margin">
                <div class="card bg-gradient-success card-img-holder text-white">
                  <div class="card-body">
                    <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/dashboard/circle.svg" class="card-img-absolute" alt="circle-image" />
                    <h4 class="font-weight-normal mb-3" style="background-color:black;">Total Moisturizer <i class="mdi mdi-pocket mdi-24px float-right"></i>
                    </h4>
                    <h2 class="mb-5" style="color:black";>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM commoist ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Combination : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM drymoist ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Dry : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM normoist ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Normal : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM oilymoist ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Oily : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM senmoist ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Sensitive : $row </p>";
                      ?>
                    </h2>
                  </div>
                </div>
              </div>
              <div class="col-md-4 stretch-card grid-margin">
                <div class="card bg-gradient-danger card-img-holder text-white">
                  <div class="card-body">
                    <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/dashboard/circle.svg" class="card-img-absolute" alt="circle-image" />
                    <h4 class="font-weight-normal mb-3" style="background-color:black;"> Total Mask <i class="mdi mdi-image-filter-vintage mdi-24px float-right"></i>
                    </h4>
                    <h2 class="mb-5" style="color:black";>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM commask ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Combination : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM drymask ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Dry : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM normask ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Normal : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM oilymask ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Oily : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM senmask ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Sensitive : $row </p>";
                      ?>
                    </h2>
                  </div>
                </div>
              </div>
              <div class="col-md-4 stretch-card grid-margin">
                <div class="card bg-gradient-info card-img-holder text-white">
                  <div class="card-body">
                    <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/dashboard/circle.svg" class="card-img-absolute" alt="circle-image" />
                    <h4 class="font-weight-normal mb-3" style="background-color:black;">Total Exfoliators & Scrubs <i class="mdi  mdi-heart mdi-24px float-right"></i>
                    </h4>
                    <h2 class="mb-5" style="color:black";>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM comex ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Combination : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM dryex ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Dry : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM norex ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Normal : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM oilyex ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Oily : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM senex ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Sensitive : $row </p>";
                      ?>
                    </h2>
                  </div>
                </div>
              </div>
              <div class="col-md-4 stretch-card grid-margin">
                <div class="card bg-gradient-info card-img-holder text-white">
                  <div class="card-body">
                    <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/dashboard/circle.svg" class="card-img-absolute" alt="circle-image" />
                    <h4 class="font-weight-normal mb-3" style="background-color:black;">Total Sunscreen <i class="mdi mdi-white-balance-sunny mdi-24px float-right"></i>
                    </h4>
                    <h2 class="mb-5" style="color:black";>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM comsun ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Combination : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM drysun ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Dry : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM norsun ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Normal : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM oilysun ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Oily : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM sensun ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Sensitive : $row </p>";
                      ?>
                    </h2>
                  </div>
                </div>
              </div>
              <div class="col-md-4 stretch-card grid-margin">
                <div class="card bg-gradient-success card-img-holder text-white">
                  <div class="card-body">
                    <img src="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/dashboard/circle.svg" class="card-img-absolute" alt="circle-image" />
                    <h4 class="font-weight-normal mb-3" style="background-color:black;">Total Eye Cream <i class="mdi mdi-star mdi-24px float-right"></i>
                    </h4>
                    <h2 class="mb-5" style="color:black";>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM comeye ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Combination : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM dryeye ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Dry : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM noreye ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Normal : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM oilyeye ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Oily : $row </p>";
                      ?>
                      <?php
                      $conn = mysqli_connect("localhost","root","","product");
                      $query = "SELECT id FROM seneye ORDER BY id";
                      $query_run = mysqli_query($conn, $query);
                      $row = mysqli_num_rows($query_run);
                      echo "<p> Sensitive : $row </p>";
                      ?>
                    </h2>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- content-wrapper ends -->
          <!-- partial:partials/_footer.html -->
          <footer class="footer">
            <div class="d-sm-flex justify-content-center justify-content-sm-between">
              <span class="text-muted text-center text-sm-left d-block d-sm-inline-block">Copyright © 2017 <a href="https://www.bootstrapdash.com/" target="_blank">BootstrapDash</a>. All rights reserved.</span>
              <span class="float-none float-sm-right d-block mt-1 mt-sm-0 text-center">Hand-crafted & made with <i class="mdi mdi-heart text-danger"></i></span>
            </div>
          </footer>
          <!-- partial -->
        </div>
        <!-- main-panel ends -->
      </div>
      <!-- page-body-wrapper ends -->
    </div>
    <!-- container-scroller -->
    <!-- plugins:js -->
    <script src="../public/PurpleAdmin-Free-Admin-Template-master/assets/vendors/js/vendor.bundle.base.js"></script>
    <!-- endinject -->
    <!-- Plugin js for this page -->
    <script src="../public/PurpleAdmin-Free-Admin-Template-master/assets/vendors/chart.js/Chart.min.js"></script>
    <!-- End plugin js for this page -->
    <!-- inject:js -->
    <script src="../public/PurpleAdmin-Free-Admin-Template-master/assets/js/off-canvas.js"></script>
    <script src="../public/PurpleAdmin-Free-Admin-Template-master/assets/js/hoverable-collapse.js"></script>
    <script src="../public/PurpleAdmin-Free-Admin-Template-master/assets/js/misc.js"></script>
    <!-- endinject -->
    <!-- Custom js for this page -->
    <script src="../public/PurpleAdmin-Free-Admin-Template-master/assets/js/dashboard.js"></script>
    <script src="../public/PurpleAdmin-Free-Admin-Template-master/assets/js/todolist.js"></script>
    <!-- End custom js for this page -->
  </body>
</html>
