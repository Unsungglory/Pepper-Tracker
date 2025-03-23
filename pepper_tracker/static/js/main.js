function openUpdateModal(cell) {
    console.log("openUpdateModal triggered");
    
    // Extract data attributes from the clicked cell
    var id = cell.getAttribute('data-id');
    var seeds = cell.getAttribute('data-seeds');
    var germinated = cell.getAttribute('data-germinated');
    var seedlings = cell.getAttribute('data-seedlings');
    var hardening = cell.getAttribute('data-hardening');
    var plants = cell.getAttribute('data-plants');
    var fruits = cell.getAttribute('data-fruits');
    var dead = cell.getAttribute('data-dead');
  
    // Get the update modal element
    var updateModal = document.getElementById('updateModal');
    if (!updateModal) {
      console.error("Update modal element not found!");
      return;
    }
    console.log("Update modal element found", updateModal);
  
    // Populate the modal fields with the data
    updateModal.querySelector('#plant_id').value = id;
    updateModal.querySelector('#seeds').value = seeds;
    updateModal.querySelector('#germinated').value = germinated;
    updateModal.querySelector('#seedlings').value = seedlings;
    updateModal.querySelector('#hardening').value = hardening;
    updateModal.querySelector('#plants').value = plants;
    updateModal.querySelector('#dead').value = dead;
    updateModal.querySelector('#fruits').value = fruits;
  
    // Update the form action URL dynamically
    var form = updateModal.querySelector('#updateForm');
    form.action = '/update/' + id;
  
    // Create a modal instance and show it
    var modalInstance = new bootstrap.Modal(updateModal);
    console.log("Modal instance created", modalInstance);
    modalInstance.show();
  }
  
  // Attach the function to the global window so it's callable from the inline onclick.
  window.openUpdateModal = openUpdateModal;
  