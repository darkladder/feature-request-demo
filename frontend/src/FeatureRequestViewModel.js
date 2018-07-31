import * as ko from 'knockout';
import jquery from 'jquery';
const $ = jquery;

function FeatureRequest($viewModel, id, title, description, client, clientPriority, targetDate, productArea) {
  this.$viewModel = $viewModel;
  
  this.id = ko.observable(id);
  this.title = ko.observable(title);
  this.description = ko.observable(description);
  this.client = ko.observable(client);
  this.clientPriority = ko.observable(clientPriority);
  this.targetDate = ko.observable(targetDate);
  this.productArea = ko.observable(productArea);

  this.isSaving = ko.observable(false);

  this.errors = ko.observable({});

  this.save = async () => {
    let errors = {};

    if (!this.title() ||
        !this.title().length) {
        errors.title = 'Title not set';
    }

    if (!this.description() ||
        !this.description().length) {
        errors.description = 'Description not set';
    }

    if (!this.client() ||
        !this.client().length) {
        errors.client = 'Client not set';
    }

    if (!this.clientPriority()) {
        errors.clientPriority = 'Client priority not set';
    }

    if (!this.targetDate() ||
        !this.targetDate().length) {
        errors.targetDate = 'Target date not set';
    }

    if (!this.productArea() ||
        !this.productArea().length) {
        errors.productArea = 'Product area not set';
    }

    if (Object.keys(errors).length) {
      this.errors(errors);
      console.warn('Could not save because of errors', errors);
      return;
    } else {
      // Clear existing errors
      this.errors({});
    }

    this.isSaving(true);

    try {
      await this.$viewModel.saveFeatureRequest(this);

      this.$viewModel.cancelEditableFeatureRequest();

    } catch (exc) {
      throw new Error(exc);
    }
    
  };

  this.cancel = () => {
    this.$viewModel.cancelEditableFeatureRequest();
  };

  this.edit = () => {
    const id = this.id();

    if (typeof id === 'undefined') {
      throw new Error('Feature request is not currently editable');
    }

    this.$viewModel.editFeatureRequest(this.id);
  };
}

class FeatureRequestViewModel {
  constructor() {
    this.clients = ko.observableArray([]);
    this.productAreas = ko.observableArray([]);

    this.availableClientPriorities = ko.observableArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  
    this.featureRequests = ko.observableArray([]);
  
    this.editableFeatureRequest = ko.observable(null);

    this.fetchSync();
  }

  async fetchSync() {
    try {
      this.fetchClients();
      this.fetchProductAreas();
      this.fetchFeatureRequests();
    } catch (exc) {
      throw new Error(exc);
    }
  }

  cancelEditableFeatureRequest() {
    this.editableFeatureRequest(null);
  }

  addFeatureRequest() {
    if (this.editableFeatureRequest()) {
      console.warn('A new feature request is currently being added');
      return;
    }

    this.editableFeatureRequest(new FeatureRequest(this));
  }

  editFeatureRequest(id) {
    let editableFeatureRequest;
    
    // Apparently KO doesn't support array maps, so we cast to a regular array
    const featureRequests = this.featureRequests();

    featureRequests.map((pos) => {
      if (pos.id === id) {
        editableFeatureRequest = pos;
      }
      
      // TODO: Break out of loop
    });

    if (editableFeatureRequest) {
      this.editableFeatureRequest(editableFeatureRequest);
    } else {
      console.warn(`Could not locate feature request with id ${id}`);
    }
  }
  
  saveFeatureRequest(featureRequest) {
    const id = featureRequest.id();
    const isNewFeatureRequest = (typeof id === 'undefined');

    const title = featureRequest.title();
    const description = featureRequest.description();
    const client = featureRequest.client();
    const clientPriority = featureRequest.clientPriority();
    const targetDate = featureRequest.targetDate();
    const productArea = featureRequest.productArea();

    // Common URL query for both types
    const urlQuery = `title=${title}&description=${description}&client=${client}&client_priority=${clientPriority}&target_date=${targetDate}&product_area=${productArea}`;

    return new Promise((resolve, reject) => {
      let jqAjax;
      if (isNewFeatureRequest) {
        // Create new feature request
        jqAajax = $.ajax({
          url: `/api/feature-request?${urlQuery}`,
          method: 'POST'
        });
      } else {
        // Edit existing feature request
        jqAjax = $.ajax({
          url: `/api/feature-request/${id}?${urlQuery}`,
          method: 'POST'
        });
      }

      jqAjax
        .done((data) => {
          console.debug(data);

          this.fetchSync();

          return resolve(true);

        })
        .fail(() => {
          return reject('Could not save');
        });
    });
  }

  fetchClients() {
    console.debug('Fetching clients');

    return new Promise((resolve, reject) => {
      $.ajax({
        url: '/api/feature-request/clients',
        dataType: 'json'
      })
      .done((data) => {
        console.debug(data);

        this.clients(data);

        resolve(true);
      })
      .fail(() => {
        return reject('Could not complete')
      });
    });
  }

  fetchProductAreas() {
    console.debug('Fetching product areas');

    return new Promise((resolve, reject) => {
      $.ajax({
        url: '/api/feature-request/product-areas',
        dataType: 'json'
      })
      .done((data) => {
        console.debug(data);

        this.productAreas(data);

        resolve(true);
      })
      .fail(() => {
        return reject('Could not complete')
      });
    });
  }

  fetchFeatureRequests() {
    console.debug('Fetching feature requests');

    return new Promise((resolve, reject) => {
      $.ajax({
        url: '/api/feature-requests',
        dataType: 'json'
      })
      .done((data) => {
        console.debug(data);

        this.featureRequests([]);

        for (let fr of data) {
          this.featureRequests.push(new FeatureRequest(this, fr.id, fr.title, fr.description, fr.client, fr.client_priority, fr.target_date, fr.product_area));
        }

        resolve(true);
      })
      .fail(() => {
        return reject('Could not complete')
      });
    });
  }
};

ko.applyBindings(new FeatureRequestViewModel());

export default FeatureRequestViewModel;